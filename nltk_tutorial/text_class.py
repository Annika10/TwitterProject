import nltk

words: list[str] = nltk.word_tokenize(
"""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""
)

text = nltk.Text(words)
# .vocab() = shortcut
fd = text.vocab()  # Equivalent to fd = nltk.FreqDist(words)
fd.tabulate(3)