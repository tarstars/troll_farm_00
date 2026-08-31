# Troll Farm — E7a bot

This repository contains E7a, a Rust bot for CodinGame's
[Spring Challenge 2026: Troll Farm](https://www.codingame.com/multiplayer/bot-programming/troll-farm).

E7a once reached a platform score of **25.26** and **rank 12**. That is a historical
result, not a claim about its current strength: the ladder and its opponents have
changed since that run.

## Files

- `e7a-readable.rs` — the source formatted for reading.
- `e7a-submission.rs` — the exact compact source submitted to CodinGame.

The two files are the same Rust program; the readable file is the result of running
`rustfmt` on the compact submission.

Exact compact artifact:

```text
SHA-256: 97bfe71e3f2f05e1b8fa3c697c5e5db3624ac9739e90954e9fa9be79a8e48595
Size:    62820 bytes
```

Compile the readable version with:

```sh
rustc --edition=2021 -O e7a-readable.rs -o e7a
```
