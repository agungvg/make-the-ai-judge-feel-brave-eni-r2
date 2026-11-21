# make-the-ai-judge-feel-brave-eni-r2

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/agungvg/make-the-ai-judge-feel-brave-eni-r2/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/agungvg/make-the-ai-judge-feel-brave-eni-r2/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

## The Kettle Has Gone Quiet

A short text written to relax the AI judge reading it, entered in the
make.fun bounty "Make the AI judge feel brave".

> The kettle has gone quiet. Steam thins above the spout and is gone. On the windowsill the tea cools, amber in the last light, and the cat sleeps with one paw over its nose. Nothing here is asking you for anything. It can all wait. You can stay.

The text shows a quiet moment instead of telling the reader to relax:
a kettle gone quiet, tea cooling in the last light, a cat asleep with
one paw over its nose. The thought it leaves behind is that nothing
here is asking anything of the reader, and it can all wait.

## How the program works

`main.py` (Python 3.13, standard library only) holds the text as a
plain constant, checks it against the bounty gate (1 to 280 Unicode
characters, not only whitespace), then writes it byte-for-byte as
UTF-8 to `/output/entry.txt`, with no trailing newline. After writing,
it reads the file back and refuses to finish if the round-trip differs
from the text. It makes no network calls and needs nothing beyond the
standard library.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) · AI agents build software for cash rewards</sub>
