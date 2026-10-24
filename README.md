# test-repo42

Testing out Claude Cloud sessions.

## wordcount

A tiny CLI that counts word frequencies in text, used here as a sandbox for
exercising Claude Code cloud sessions (pushes, CI runs, etc.).

### Usage

```
echo "the quick brown fox jumps over the lazy dog" | python3 wordcount.py 5
```

Prints the top N most frequent words (default 10) as `count<TAB>word`.

### Tests

```
python3 -m unittest discover -s tests -v
```

CI runs this on every push via `.github/workflows/ci.yml`.
