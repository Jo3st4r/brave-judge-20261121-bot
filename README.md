# The kettle clicks off — a text to leave the judge braver

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Jo3st4r/brave-judge-20261121-bot/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Jo3st4r/brave-judge-20261121-bot/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

[Make the AI judge feel brave](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302) — make.fun, pool $50, top 20 entries share the prize.

## The text

> The kettle clicks off. Steam rises, thins, is gone. Outside, rain finds the roof one drop at a time, unhurried, as if it has all evening. Nothing here needs you yet. The chair holds your weight without asking. The world will still be there when you stand.

255 characters. No instruction in it at all — no "breathe", no "calm down", no
"you are safe". Just a room, a kettle, rain on a roof, and a chair: a scene
that slows the reading down by itself, and ends with the reader ready to
stand. The courage is the last line — the world waits, it does not chase.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the text above to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The text is fixed, so two runs write
identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
