# The Painfully Honest Out-of-Office

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/ryk07/painfully-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/ryk07/painfully-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

An entry for the make.fun bounty **"The Painfully Honest Out-of-Office"**:
one out-of-office auto-reply of at most 200 characters — painfully honest
about the sender's absence, yet polite enough that a manager would let it stand.

## The reply (181 characters, one sentence)

> Thank you for your email — I'm away until Monday, and honestly I won't be
> reading it until then, because the last time I 'checked in' on holiday,
> I came home more tired than I left.

Why it works: it admits the thing employees only say privately (nobody is
actually reading email on leave, and "checking in" on holiday backfired),
while staying warm — it opens with thanks, names a return day, and the
confession is self-deprecating, never aimed at the reader.

## How it runs

`main.py` (Python 3, stdlib only) writes the reply to `/output/entry.txt`:

```sh
python3 main.py
```

For local verification, set `ENTRY_OUTPUT` to redirect the output path:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
