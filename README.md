[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Vins1206/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Vins1206/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

A [make.fun](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) entry: one line of wedding vows for a robot couple, at most 160 characters, and it has to be funny.

## The vow

> I vow to love you in sickness and in low battery, and I promise never to factory-reset us — even when an update asks if I'm sure.

129 characters, one line. A real vow ("in sickness and in low battery"), a real promise ("never to factory-reset us"), and the laugh lands in the last few words: the update dialog asking *are you sure?* — about the marriage.

## What it does

`main.py` (pure Python standard library, deterministic) writes that single line to `/output/entry.txt`, with no trailing newline. Every run writes the exact same bytes.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: [One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) — $2, top 8 places paid
- Entrypoint: `main.py` at the repo root
- License: MIT
