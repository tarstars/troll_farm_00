# Troll Farm: hypotheses tried, in chronological order

Status: 1 September 2026, through V418

This is a plain-language history for somebody new to the project. It records the ideas we tested, why we tested them, what happened, and what we learned.

## How to read this document

- A **hypothesis** is simply an idea that might make the bot win more often.
- A name such as **V10** is an experiment label. It is not a game rule or a release promised to users.
- Many consecutive labels test tiny variations of the same idea. They are grouped together here so the main story remains visible.
- Some labels are skipped because they were packaging checks, exact copies, or experiments stopped before they became a distinct idea.
- Candidate and platform numbers can differ. For example, candidate V416 was the code submitted as platform V417.
- A **local test** is a repeatable set of simulated games. A **platform result** is the real CodinGame ladder result.
- A local score margin tells us how many more game points the bot earned. The platform rank depends mainly on wins, draws, and losses, so later tests count outcomes first.
- A platform result is called mature only after all games and the platform's rank-stabilization process are finished.

## Starting point: the bot before these experiments

The base bot usually plays with two trolls. It cuts trees, banks wood, sometimes runs a small apple orchard, and applies limited pressure to trees that the opponent planted. It already contains several old farming ideas. New work therefore has to improve it without breaking its useful opening or sending trolls away from normal chores.

The target for this cycle is a mature platform score of at least 25 and a rank below 10.

## V1-V2: a large renewable banana farm

**Belief.** A renewable banana plantation would create enough fruit and wood to overpower the simpler resident bot.

**What changed.** V1 added a substantial banana-farm plan. In local games it looked spectacular: it improved all 72 sampled maps and beat the resident bot in most direct games. V2 removed that farm and kept smaller, older improvements to tree pressure and late banking.

**What happened.** V1 collapsed on the real platform and was replaced early at score 13.20. V2 matured at score 23.03, rank 32.

**Lesson.** The local simulator greatly overvalued the exposed plantation. A large farm can give the opponent fruit and time as well as helping us. From this point onward, real replays and fixed-map comparisons became essential.

## V3-V4: copy decisions from strong players

**Belief.** Strong players had already discovered better worker builds and tree choices, so copying visible choices from their replays should improve our bot.

**What changed.** V3 copied learned tree decisions. V4 changed which second troll to train, following examples from a strong player.

**What happened.** V3 scored only 17.28 online. V4 was inconsistent and worse overall.

**Lesson.** A worker build or tree choice only makes sense together with the strategy around it. Copying one visible decision without the rest of the plan does not copy the strength of the original bot.

## V5-V9: make a three-troll fruit factory work

**Belief.** A fruit factory could pay for a third troll, and the extra troll would provide the production missing from the two-troll bot.

**What changed.** These versions tried several crop lifecycles, crop ownership rules, fruit reserves, harvesting delays, banking rules, and protection of original trees.

**What happened.** Some versions created much more material for us, but they also reduced pressure on the opponent. The opponent often gained even more. None was safe enough for the ladder.

**Lesson.** Production and interference with the opponent cannot be separated. A farm that occupies the first two trolls may fund a third troll and still lose the game before that investment pays back.

## V10-V12: repair the factory lifecycle

**Belief.** The factory idea was sound, but its workers were harvesting, banking, or choosing planting cells incorrectly.

**What changed.** V10 copied the observed farming rhythm more closely. V11 removed V10's mistake of always cutting our own crop first. V12 changed how planting locations were chosen, preferring total travel cost rather than one part of the trip.

**What happened.** V10 lost badly in fixed-map platform tests. V11 looked better in the simulator after freeing the trapped worker, but still lost badly in real fixed-map tests. V12 was clearly worse even locally.

**Lesson.** V10's problem was not a single broken detail. V11 repaired a real worker-control error, but the overall factory still gave up too much map pressure. V12 confirmed that a small placement rule could not rescue the architecture.

## V13-V31: balanced factories, lean farms, and a dedicated worker

**Belief.** The factory might work if the third troll were balanced, or if the farm were much smaller and used a dedicated nearby worker.

**What changed.** V13-V23 tried balanced three-worker factories. V24-V29 reduced the farm and changed when it began. V30-V31 tried to buy a worker specifically for the small farm, then made that worker cheaper by reducing movement skill.

**What happened.** The exposed crops remained profitable for strong opponents. The dedicated worker never trained in 384 games because its bill was still too expensive for the supplies available without a harmful detour.

**Lesson.** The missing third troll is not free spare capacity. Paying for it changes the whole opening. A worker designed only for the home area can still be unaffordable if the first two trolls must stop useful work to fund it.

## V32-V47: harvest more and finish opponent crops

**Belief.** Losses showed missing fruit and opponents with productive crops. More harvesting, stronger crop cutting, or finishing a nearly cut tree might close the gap.

**What changed.** These versions tried a harvesting second troll, harvesting without the apple orchard, stronger pressure on opponent crops, early nursery attacks, limited pressure windows, and special rules for the last cut on apple, lemon, or focused trees.

**What happened.** Broad pressure often helped the opponent by finishing a tree and releasing wood at the wrong time. Broad harvesting sent trolls on detours. Narrow rules were safer but too rare.

**Lesson.** A replay symptom is not automatically a useful action. Opponent crops are common in losses partly because strong opponents grow them well. Chasing the symptom can make our own schedule worse.

## V48-V66: smaller local farms and contested-tree rules

**Belief.** A farmer close to home, plus very focused tree contests, could add production without the cost of the large factory.

**What changed.** V48-V53 tried local farmers and last-cut rules for opponent bananas. V54-V66 tested persistent focus only while already on a tree, softer versions of that focus, apple contests, distance limits, ripeness checks, and combinations with the older reliable tree preference.

**What happened.** The safest result became V54: a small, guarded preference rather than a broad route change. Both removing that preference and increasing it later proved worse.

**Lesson.** The useful middle ground is small. Staying on a tree can be good when the troll is already there, but turning it into a general destination changes too many later actions.

## V67-V107: the long search for a truly lean banana farm

**Belief.** The original farm was too large and clumsy. A lean version should use one or two mother banana trees near home, harvest them repeatedly, plant only nearby chop trees, and preserve a clear banking route.

**What changed.** This family tried safe start checks, observed opponent activity, enemy travel time, immediate child planting, holding a doorway briefly, waiting for full-grown children, exact banking, reachable chop plots, earlier starts, apple-orchard combinations, free-worker behavior during growth, mother-aware routes, different doors, cleanup timing, scarce-map rules, and several ways to provide banana seeds.

**What happened.** Individual replays looked much better, but wider tests repeatedly showed the same tradeoff: our farm raised our output while giving production-focused opponents even more time and value. V100 became the best distinct fallback, but the V108 banana-supply extension matured at only 22.90, rank 32.

**Lesson.** Better farm geometry does not solve bad timing. A small plantation can still be too expensive if it replaces tree pressure or starts after the opponent's economy is already growing.

## V108-V125: rechecks and replay diagnosis

**Belief.** Platform noise might be hiding a good older version, and the failed farm starts might have one simple cause.

**What changed.** We reran exact older bots and tested cheaper banana supply, orchard cost filters, ownership-only commitments, no-farm variants, first-harvest time limits, keeping the farmer beside the mother, and harvesting before emergency cleanup.

**What happened.** Exact rechecks still varied: V115 scored 23.53/rank 29, V121 22.92/rank 31, and V125 23.76/rank 26. Disabling the lean farm lost locally, even though its few platform starts were losses. Fixed time limits also removed useful starts. Harvesting before emergency cleanup let opponents gain more than us.

**Lesson.** A feature appearing mostly in losses does not prove that the feature caused them. Exact A/B tests are needed. Platform scores also move enough that repeating identical code does not guarantee the same rank.

## V127-V159: replace one job score with explicit priorities

**Belief.** The bot gave every possible job one numeric weight. A high-quality low-priority job might therefore beat an urgent job. A priority list could separate urgency from quality.

**What changed.** V127 and platform V133 compared job pairs by: first job priority, second job priority, and only then the old quality score. Later versions made the rule stricter or softer, extended it to other worker counts, or used it only before turn 200. At the same time, V138-V159 combined the priority system with compact two-mother, one-mother, sparse-map, orchard-first, and idle-only banana farms.

**What happened.** The priority list removed many waits and had a small positive local result, but V133 matured at 22.30/rank 35. Strict priority separation was too rigid. The best compromise used priorities before turn 200 and the old score late, because late trips often could not pay back. Compact farms could gain locally, but wider tests showed they still displaced useful work. An idle-only farm was safe but almost never active.

**Lesson.** Explicit priorities are clearer and can prevent some interference, but job selection was not the main platform weakness. A good priority system cannot make an expensive farm cheap.

## V163-V186: one mother tree, normal chores between farm actions

**Belief.** The farm should act only when planting or harvesting is immediately possible. During growth and cooldown, the farmer should return to ordinary work.

**What changed.** We tested banana instead of the apple orchard, a copied hybrid worker, one mother with one or two neighboring chop plots, stronger opponent-crop preference, race checks, protected seed handling, early-start guards, and windows that brought the farmer back shortly before fruit appeared.

**What happened.** V169 greatly improved the farm's visible lifecycle in a few games, but lost 1,102 total margin in the wider screen. Guarded versions reduced the damage without removing it. V178 cut many idle turns but still lost in the large confirmation. Return-window versions remained too disruptive.

**Lesson.** Avoiding idle time is necessary, but not sufficient. Even a worker doing normal chores between farm steps can arrive late to contested trees because the farm changes its location and inventory.

## V187-V211: one banana tree on a tent entrance

**Belief.** A super-light farm could behave like a small tax on normal traffic. No troll would be assigned to it. When a troll naturally stepped onto the selected tent entrance, one farm transition would occur: plant, harvest, bank three bananas, chop, bank wood, and return to an empty cell.

**What changed.** Early versions reserved the cell or reacted merely to standing on it. Later versions required a real arrival, return traffic, a third troll, a banana already being carried home, a repeat visit by the same capable troll, and distance from enemy cutters.

**What happened.** Reserving or reacting to the cell changed ordinary work and lost thousands of points. Triggering only on return traffic preserved the opening but still delayed arrival at contested trees. Starting after a third troll was safe but almost never happened. Planting with a banana already being carried was the lightest version, but none of these farms completed the full three-banana cycle reliably.

**Lesson.** The finite-state idea is sound, but an action is never truly free: each troll gets only one action per turn. The tree often worked as cheap wood or bait, not as a renewable fruit farm.

## V212-V230: fund a third troll without breaking the first two

**Belief.** If the first two trolls left the correct fruit in the tent, a third troll could be trained without a large dedicated farm.

**What changed.** We split worker skills, restored the older three-troll factory, added modern opponent-tree pressure, tried cheaper third trolls, deadlines, funding cutoffs, and shared harvesting. We also rechecked old E7a and other complete production bots. V228-V230 revisited local banana harvesting and explicit priorities.

**What happened.** The best old factory trained a third troll in 61 of 96 games and raised our score by 3,456, but opponents gained 5,167. Modern tree pressure recovered much of the loss, not all of it. Cheaper workers were too weak; deadlines wasted investments already made; shared funding interrupted essential pressure. Old E7a's historic 25.26 was not repeatable evidence for the current ladder. Full priority lists changed no commands in the observed games.

**Lesson.** A third troll is valuable only if it arrives early and the first two trolls keep contesting the map. Funding, worker design, and opponent pressure form one complete strategy and cannot be safely copied one piece at a time.

## V231-V247: a strict arrival-only entrance tax

**Belief.** The entrance farm could be made safe if the ordinary planner ran first and the farm never routed, reserved, or held a troll.

**What changed.** V231 wrapped the ordinary bot and acted only after a real arrival at the chosen door. V232-V235 tried to protect the tree from ordinary chopping. V236 skipped the tax while behind. Later versions tried stronger cutters, time-limited protection, and focused collection for a cheap third troll.

**What happened.** V231 had a real local gain and matured at 24.01/rank 25. Replays showed why: our bot planted the entrance banana and then usually cut it before harvesting fruit. The gain came from a cheap disposable tree, not the requested farm cycle. Protecting it lost because immediate wood was worth more than rare future fruit. V236 matured at 23.05/rank 29. Focused third-worker collection lost heavily.

**Lesson.** A strict action tax can be safe and useful, but preserving the tree changes ordinary work. The simple bot benefits more from quick wood than from waiting for a perfect three-fruit lifecycle.

## V248-V258: let the apple orchard start on more maps

**Belief.** The apple orchard was being blocked by old fixed distance rules even when the actual enemy was far enough away.

**What changed.** These versions removed several orchard vetoes one by one, reduced a fixed enemy-door distance, and finally relied on the live enemy travel-time check instead of the old map-only limit.

**What happened.** Local score margins improved greatly, but platform results were mixed: V248 22.45/rank 32, V251 23.81/rank 27, V256 23.65/rank 28, and V258 24.59/rank 21.

**Lesson.** The orchard really was more productive, but raw game-point gains did not consistently create more wins. This led to a major testing change: choose candidates by wins, draws, and losses first; use score margin only as a safety check.

## V259-V310: outcome-first, narrow tactical changes

**Belief.** Small, guarded actions could convert close losses without disturbing established wins.

**What changed.** This long family tested orchard deadlines, small entrance-tax deficit limits, early pressure on an opponent who was saving resources, time windows, tree-reach limits, enemy-first penalties, contested harvests, water-side door preferences, worker builds, and many combinations. V266 reopened the disposable entrance tree only while no more than eight points behind. V273 kept a useful opponent-pressure signal only during turns 11-32. V274 combined them. V279-V310 mined specific replay moments with progressively narrower rules.

**What happened.** Many changes looked positive in a small screen and then destroyed one established win in the larger confirmation. V266 matured at 22.85/rank 30 and V274 at 23.32/rank 28. The safe endpoints were narrow: do not widen the deficit limit, pressure window, or tree reach without new evidence.

**Lesson.** Protecting existing wins is more important than accumulating raw margin. A candidate with five new wins and one lost established win can still be too risky when that loss exposes a broad failure mode.

## V311-V330: take fruit only when ordinary work would wait

**Belief.** Harvesting could be almost free if a troll was already standing on the tree and the completed ordinary plan told it to wait.

**What changed.** V311 took the final fruit from a damaged opponent-planted tree that an enemy was already chopping. V313 broadened this to any ripe tree. V314 kept only apples. V315 removed a useless last-turn harvest. V316-V326 rechecked protected entrance farms, cash-out timing, and the old factory. V327-V330 tested idle help on own or contested trees.

**What happened.** V311 matured at 24.67/rank 22. Broad harvesting lost an established win; apple-only harvesting was locally stronger but matured at 22.72/rank 30 and almost never activated in the live mix. Protecting the entrance farm failed again. A broader contested-tree helper changed many commands but lost match points.

**Lesson.** A true final-wait replacement is one of the safest ways to add behavior. Even so, a rare safe action may not move the platform rank, and broadening it by fruit type or tree ownership quickly stops being free.

## V331-V353: copy a top player's bounded home farm

**Belief.** A top-eight two-troll bot showed a real continuous local farm: one troll planted and harvested near home while a trained cutter made wood. Copying its bounded geometry and worker might provide the missing production.

**What changed.** V331-V341 built and repaired an eight-tree nearby farm. V342-V347 enabled it only as a comeback plan. V348-V349 copied the observed 2/2/0/2 cutter. V350 and V353 then restored the best older small-action bots for clean platform rechecks. V351 directly tested whether priority interference caused the scaling losses; V352 tried abandoning a losing orchard.

**What happened.** The corrected farm increased our raw production but lost matches because it replaced cross-map pressure. The comeback guard passed development and failed the large confirmation badly. The copied worker was harmful without the source bot's complete opening. V350, an exact V311 recheck, matured at 24.79/rank 20; V353 at 23.22/rank 29. The priority change affected no relevant games, and abandoning the orchard often produced a wait rather than useful work.

**Lesson.** A successful worker and farm belong to a full strategy. The current bot's main scaling problem is not that its one-number job weights are visibly crossing priorities in those states.

## V354-V381: stop trolls from blocking the tent

**Belief.** Some close losses came from a concrete movement failure: a troll carrying wood repeatedly backed away from the tent because another troll occupied the needed entrance.

**What changed.** V354 tried a general doorway swap. V355 allowed it only with exactly two trolls, a returning wood carrier, and an empty waiting blocker that could safely swap places. Later versions added a narrow crop-finishing action for close games, then allowed collection only after the opening.

**What happened.** The narrow swap repaired the exact replay and was safe locally, but platform V356 matured at 22.60/rank 30 because the event was rare. V370's close-game crop finish reached 25.21/rank 17, the first mature run to clear the score half of the target, although that new action never actually fired in the live games. V381's opening-safe collection matured at 24.73/rank 22.

**Lesson.** Concrete replay fixes are safer than broad strategy changes, but a rare fix cannot carry the whole rank. It remains worth keeping if it does not damage normal games.

## V382-V404: react when the opponent trains more trolls

**Belief.** The clearest remaining loss pattern was opponent scaling: our bot stayed at two trolls while strong opponents reached three or four. We might answer with stronger crop pressure or a conditional production plan.

**What changed.** We tested wider crop-finishing limits, actions while sharing a tree with an enemy, funding a cheap third troll after seeing the opponent scale, assigning funding to different workers, a one-iron bridge, and stronger pressure specifically against dedicated harvesters. V399-V404 revisited bounded farming only in severe late states.

**What happened.** Third-worker funding damaged many games. A bridge that looked almost affordable still helped the opponent more. General pressure was unsafe; specialist-only pressure passed local tests but platform V392 matured at 21.15/rank 38 because it changed only two live games. Conditional late farms were either dormant or lost when replayed against independent older archives.

**Lesson.** Seeing the opponent's third troll does not make our own funding bill cheaper. Rules selected from a few current losses must also survive older independent games.

## V405-V409: return to actions that do not reroute trolls

**Belief.** The safest remaining changes would replace only a wait or an action already happening underfoot.

**What changed.** V405 broadened the final-wait harvest. V406-V408 tried harvesting before a contested chop, with score and opponent-count guards. V409 tried to save ripe fruit on the passive entrance banana immediately before our own chop.

**What happened.** V405 was safe but never activated. The contested-harvest versions delayed a useful chop and lost outcomes in independent continuations. V409 was completely inactive because the tree was normally cut before fruit survived to that decision point.

**Lesson.** A change can be perfectly safe and still useless. Repairing the visible final symptom is too late if the cause happened many turns earlier.

## V410-V418: escape long doorway loops, but only after proof

**Belief.** A broader version of the proven tent swap could rescue trolls stuck for dozens or hundreds of turns, including a doorway troll that was harvesting or depositing and an empty trapped chopper.

**What changed.** V410 allowed a harvesting blocker but never fired because the actions were out of phase. V411 included a depositing blocker and rescued the long stall, but firing after one backtrack was unsafe. V412 added a 32-repeat wait but accidentally delayed the old proven swap too. V413 corrected that mistake and became platform V414. V415 required the stuck carrier to hold at least two wood. V416 also rescued an empty trapped worker after 32 repeats and became platform V417. V418 tried triggering after only 16 repeats.

**What happened.** V414 matured at 22.66/rank 32. The two-wood rule removed small one-wood regressions. V416 passed fresh games and exact continuation tests: before maturity, its first three live activations added one win and no lost outcome in replay continuations. V418 was rejected because the earlier trigger created four worse outcomes in older archives.

**Lesson.** Waiting for repeated evidence is important. The 32-repeat guard looks conservative, but the 16-repeat experiment proved that acting sooner can interrupt a loop that would have resolved safely.

## Platform result snapshot

These are selected mature runs, not every local experiment:

- V2: 23.03, rank 32
- V125: 23.76, rank 26
- V152: 22.72, rank 30
- V231: 24.01, rank 25
- V258: 24.59, rank 21
- V274: 23.32, rank 28
- V311: 24.67, rank 22
- V350: 24.79, rank 20
- V356: 22.60, rank 30
- V370: 25.21, rank 17
- V381: 24.73, rank 22
- V392: 21.15, rank 38
- V414: 22.66, rank 32
- V417: still stabilizing when this document was written; early rank is not a mature result

## What the project now believes

1. Large or dedicated farms are usually too expensive for this two-troll opening.
2. A farm can raise our score and still make us less likely to win because the opponent gets time, fruit, or uncontested trees.
3. A copied worker or rule from a top bot is not portable without the rest of that bot's strategy.
4. Explicit job priorities are clearer than one mixed number, but they were not the main scaling problem in the tested states.
5. Actions that happen only after normal planning, especially replacing a final wait, are the safest additions.
6. Concrete replay fixes should be narrow, delayed until the failure is undeniable, and checked against independent older games.
7. Local raw score is not enough. Wins, draws, losses, exact live activations, and mature platform rank are the real tests.
8. Rank stabilization must finish before a candidate is called successful.

## The open problem

The bot can reach score 25, but has not yet matured below rank 10. Its hardest losses still combine two facts: the opponent grows to three or four useful trolls, while our two trolls must keep both producing and contesting the map. The next successful change probably needs either a genuinely cheap way to scale or a stronger complete two-troll plan. It must not pay for that improvement by abandoning normal chores.
