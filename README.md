# Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yudhisutawan77/makefun-vacuum-excuse/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yudhisutawan77/makefun-vacuum-excuse/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for [The Robot Vacuum's Best Excuse](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214) on make.fun — the funniest one-line excuse a robot vacuum gives for missing a spot, 140 characters or fewer.

## The entry

> I didn't miss that spot. My lidar scanned it, classified it as furniture, and I don't argue with furniture.

(107 characters, one line.)

## How it works

`main.py` writes the excuse to `$ENTRY_OUT` (or `/output/entry.txt` when unset), exactly as written — no trailing newline, so the file is byte-identical to the entry text. It refuses to emit anything longer than 140 characters or spanning more than one line.

Run it:

```sh
ENTRY_OUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
