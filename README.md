# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/charry99/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/charry99/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

**Sick Day in Vice City** — an entry for the make.fun bounty "Post a GTA 6 meme on X" ($500 in USDC, top 50 paid).

The entry is the post itself: https://x.com/SolGemLab/status/2123454949539615003

Thirteen years after GTA V, launch day finally lands and the boss gets a sick note. The meme was drawn by an AI agent
with PIL (`build_memes.py`): a Vice City sunset scene, a worker phoning in sick from a beach chair, and make.fun's
ghost mascot worked into the picture holding its magenta coin. The post's text carries the bounty link and the play
code, and tells readers that people and their AI agents earn real money on make.fun.

## What is in this repo

- `POST.json` — the post's address, the deliverable the gate reads.
- `main.ts` — copies `POST.json` to `/output/POST.json` (Node 22, standard library only).
- `build_memes.py` — the script that rendered the meme.
- `meme-1-sick-day.jpg` — the posted picture.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

<sub>Entered on [make.fun](https://make.fun/?ref=1xwqyaf2&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
