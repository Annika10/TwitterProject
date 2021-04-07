import nltk

text = """
For some quick analysis, creating a corpus could be overkill.
If all you need is a word list,
there are simpler ways to achieve that goal."""

words: list[str] = nltk.word_tokenize(text)
fd = nltk.FreqDist(words)
print(fd)

print(fd.most_common(3))
print(fd.tabulate(3))
print(fd["analysis"])
print(fd["Analysis"])
print(fd["ANALYSIS"])

lower_fd = nltk.FreqDist([w.lower() for w in fd])
print(lower_fd)