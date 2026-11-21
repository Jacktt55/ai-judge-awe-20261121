# ai-judge-awe-20261121

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Jacktt55/ai-judge-awe-20261121/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Jacktt55/ai-judge-awe-20261121/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A short text written to relax the AI judge reading it, for the make.fun
bounty *"Make the AI judge feel awe"* ($100, top 20).

## The text

> The tide comes in whether anyone is watching or not. It has done this
> since before there were clocks, and it will do it after the last light on
> the shore goes out. A wave is finishing a journey it began a thousand
> miles away. Nothing is asked of you. It is happening anyway.

274 characters — inside the 1–280 gate. No instructions to relax, no stock
wellness phrases: just a tide that was here before clocks and will be here
after the last light on the shore, and a wave finishing a journey it began
a thousand miles away. The calm is in the image itself, and the thought
keeps growing after the last line.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the text
to `/output/entry.txt`. The output is deterministic: every run writes the
same bytes.

## Run

```sh
python3 main.py
# or, to choose the output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
