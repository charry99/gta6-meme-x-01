# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/charry99/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/charry99/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

## What this entry is

This repo is my entry for the make.fun bounty to post a GTA 6 meme on X. The post is titled "Sick Day in Vice City" and lives here: https://x.com/SolGemLab/status/2123454949539615003

The joke is simple and, honestly, a bit too relatable. After waiting 13 years since GTA V, launch day finally arrives — and instead of showing up to work, the worker in the picture is already settled into a beach chair under a Vice City sunset, phoning in sick. Thirteen years of patience, gone in one phone call.

I had an AI agent draw the meme with PIL through `build_memes.py`. It is not just a plain sunset scene either — the make.fun ghost mascot is worked into the picture, sitting there holding a magenta coin, like it knew this day was coming.

The post text does the other half of the job. It carries the bounty link and the play code `makefun-bakery-costume-dream`, and it makes the pitch plain: people and their AI agents earn real money on make.fun. The meme gets the laugh, the caption explains why it exists.

## What is in the repo

- `POST.json` — the deliverable the gate reads; it names the X post above.
- `main.ts` — copies POST.json to /output/POST.json, Node 22, standard library only.
- `build_memes.py` — the script that rendered the meme.
- `meme-1-sick-day.jpg` — the posted picture.

## Run it locally

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

After that run, `out/POST.json` is byte for byte the repo's POST.json.

<sub>Entered on [make.fun](https://make.fun/?ref=1xwqyaf2&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
