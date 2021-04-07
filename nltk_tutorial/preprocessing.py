import nltk
from pprint import pprint

# isalpha = no punctuation words
words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]

print(words)

# remove stop words like “of,” “a,” “the,”
stopwords = nltk.corpus.stopwords.words("english")
words = [w for w in words if w.lower() not in stopwords]

# split raw text into individual words
text = """
For some quick analysis, creating a corpus could be overkill.
If all you need is a word list,
there are simpler ways to achieve that goal."""
pprint(nltk.word_tokenize(text), width=79, compact=True)
