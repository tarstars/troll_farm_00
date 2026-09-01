#!/usr/bin/env python3
"""Build the plain-language hypotheses PDF without external dependencies."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


PAGE_W = 595.28
PAGE_H = 841.89
LEFT = 54.0
RIGHT = 54.0
TOP = 58.0
BOTTOM = 48.0


def pdf_text(value: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u2192": "->",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = value.encode("latin-1", "replace").decode("latin-1")
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def width(text: str, size: float) -> float:
    # A conservative Helvetica estimate. It intentionally wraps a little early.
    units = 0.0
    for char in text:
        if char in " il.,:;'|!":
            units += 0.28
        elif char in "MW@%":
            units += 0.86
        elif char.isupper():
            units += 0.64
        else:
            units += 0.52
    return units * size


def wrap(text: str, size: float, available: float) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = current + " " + word
        if width(trial, size) <= available:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


@dataclass
class Page:
    commands: list[str]


class Layout:
    def __init__(self) -> None:
        self.pages: list[Page] = []
        self.page: Page | None = None
        self.y = PAGE_H - TOP
        self.new_page()

    def new_page(self) -> None:
        self.page = Page([])
        self.pages.append(self.page)
        self.y = PAGE_H - TOP

    def ensure(self, height: float) -> None:
        if self.y - height < BOTTOM:
            self.new_page()

    def text(self, x: float, y: float, value: str, font: str, size: float, color: str = "0 0 0") -> None:
        assert self.page is not None
        self.page.commands.append(
            f"BT /{font} {size:.2f} Tf {color} rg 1 0 0 1 {x:.2f} {y:.2f} Tm ({pdf_text(value)}) Tj ET"
        )

    def line(self, x1: float, y1: float, x2: float, y2: float, color: str = "0.75 0.78 0.82") -> None:
        assert self.page is not None
        self.page.commands.append(f"{color} RG 0.7 w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def paragraph(self, text: str, *, indent: float = 0.0, bullet: bool = False) -> None:
        size = 10.35
        leading = 14.1
        bullet_gap = 13.0 if bullet else 0.0
        available = PAGE_W - LEFT - RIGHT - indent - bullet_gap
        lines = wrap(text, size, available)
        self.ensure(len(lines) * leading + 5)
        if bullet:
            self.text(LEFT + indent, self.y, "-", "F2", size)
        x = LEFT + indent + bullet_gap
        for line in lines:
            self.text(x, self.y, line, "F1", size, "0.08 0.10 0.13")
            self.y -= leading
        self.y -= 4.0

    def heading(self, level: int, text: str) -> None:
        if level == 1:
            if len(self.pages) > 1 or self.y < PAGE_H - TOP - 1:
                self.new_page()
            size, leading, before, after = 24.0, 29.0, 0.0, 16.0
            color = "0.08 0.25 0.42"
        elif level == 2:
            size, leading, before, after = 15.0, 19.0, 11.0, 8.0
            color = "0.08 0.31 0.50"
        else:
            size, leading, before, after = 12.0, 16.0, 7.0, 5.0
            color = "0.12 0.34 0.49"
        lines = wrap(text, size, PAGE_W - LEFT - RIGHT)
        self.ensure(before + len(lines) * leading + after + (18 if level == 2 else 0))
        self.y -= before
        for line in lines:
            self.text(LEFT, self.y, line, "F2", size, color)
            self.y -= leading
        if level == 2:
            self.line(LEFT, self.y + 4, PAGE_W - RIGHT, self.y + 4)
        self.y -= after


def parse_markdown(path: Path) -> Layout:
    layout = Layout()
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            layout.paragraph(" ".join(paragraph))
            paragraph.clear()

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line == "---":
            flush()
            layout.ensure(12)
            layout.line(LEFT, layout.y, PAGE_W - RIGHT, layout.y)
            layout.y -= 12
            continue
        match = re.match(r"^(#{1,3})\s+(.*)$", line)
        if match:
            flush()
            layout.heading(len(match.group(1)), match.group(2))
            continue
        if line.startswith("- "):
            flush()
            layout.paragraph(line[2:], indent=8, bullet=True)
            continue
        match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if match:
            flush()
            layout.paragraph(f"{match.group(1)}. {match.group(2)}", indent=8)
            continue
        paragraph.append(line)
    flush()
    return layout


def build_pdf(layout: Layout, output: Path) -> None:
    objects: list[bytes] = []

    def add(value: bytes) -> int:
        objects.append(value)
        return len(objects)

    catalog_id = add(b"")
    pages_id = add(b"")
    font_regular = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    font_bold = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
    page_ids: list[int] = []

    for number, page in enumerate(layout.pages, 1):
        # Header and footer are added after layout so they are identical on every page.
        page.commands.insert(
            0,
            f"BT /F1 8.2 Tf 0.40 0.45 0.50 rg 1 0 0 1 {LEFT:.2f} {PAGE_H - 29:.2f} Tm (Troll Farm hypotheses timeline) Tj ET",
        )
        page.commands.append(
            f"BT /F1 8.2 Tf 0.40 0.45 0.50 rg 1 0 0 1 {PAGE_W - RIGHT - 46:.2f} 25 Tm (Page {number} of {len(layout.pages)}) Tj ET"
        )
        stream = ("\n".join(page.commands) + "\n").encode("latin-1")
        content_id = add(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"endstream")
        page_id = add(
            (
                f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {PAGE_W:.2f} {PAGE_H:.2f}] "
                f"/Resources << /Font << /F1 {font_regular} 0 R /F2 {font_bold} 0 R >> >> "
                f"/Contents {content_id} 0 R >>"
            ).encode("ascii")
        )
        page_ids.append(page_id)

    objects[pages_id - 1] = (
        f"<< /Type /Pages /Count {len(page_ids)} /Kids [{' '.join(f'{value} 0 R' for value in page_ids)}] >>"
    ).encode("ascii")
    objects[catalog_id - 1] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("ascii")

    payload = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(payload))
        payload.extend(f"{index} 0 obj\n".encode("ascii"))
        payload.extend(obj)
        payload.extend(b"\nendobj\n")
    xref = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    payload.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode("ascii")
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(payload)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    source = root / "docs/hypotheses-tried.md"
    output = root / "docs/hypotheses-tried.pdf"
    layout = parse_markdown(source)
    build_pdf(layout, output)
    print(f"wrote {output} ({len(layout.pages)} pages, {output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
