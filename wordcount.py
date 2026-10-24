"""Count word frequencies in text."""

import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[a-zA-Z']+")


def tokenize(text):
    return [word.lower() for word in WORD_RE.findall(text)]


def count_words(text):
    return Counter(tokenize(text))


def top_words(text, n=10):
    return count_words(text).most_common(n)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    n = int(argv[0]) if argv else 10

    text = sys.stdin.read()
    for word, count in top_words(text, n):
        print(f"{count}\t{word}")


if __name__ == "__main__":
    main()
