import unittest

from wordcount import count_words, tokenize, top_words


class TestTokenize(unittest.TestCase):
    def test_splits_on_punctuation(self):
        self.assertEqual(tokenize("Hello, world!"), ["hello", "world"])

    def test_lowercases(self):
        self.assertEqual(tokenize("Claude CLAUDE claude"), ["claude", "claude", "claude"])

    def test_keeps_apostrophes(self):
        self.assertEqual(tokenize("it's a test"), ["it's", "a", "test"])

    def test_empty_string(self):
        self.assertEqual(tokenize(""), [])


class TestCountWords(unittest.TestCase):
    def test_counts_frequencies(self):
        self.assertEqual(count_words("a a b"), {"a": 2, "b": 1})


class TestTopWords(unittest.TestCase):
    def test_returns_most_common_first(self):
        text = "cloud cloud cloud session session test"
        self.assertEqual(top_words(text, 2), [("cloud", 3), ("session", 2)])

    def test_respects_limit(self):
        text = "a b c"
        self.assertEqual(len(top_words(text, 1)), 1)


if __name__ == "__main__":
    unittest.main()
