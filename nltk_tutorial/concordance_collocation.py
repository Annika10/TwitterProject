import nltk

# concordance = collection of word locations along with their context
# 1. How many times a word appears
# 2. Where each occurrence appears
# 3. What words surround each occurrence

# doesn't care case
# only prints
text = nltk.Text(nltk.corpus.state_union.words())
text.concordance("america", lines=5)

# more usable + sorted
print()
concordance_list = text.concordance_list("america", lines=2)
for entry in concordance_list:
    print(entry.line)

# collocations = series of words that frequently appear together
# Bigrams: Frequent two-word combinations
# Trigrams: Frequent three-word combinations
# Quadgrams: Frequent four-word combinations

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
finder = nltk.collocations.TrigramCollocationFinder.from_words(words)
print(finder.ngram_fd.most_common(2))
print(finder.ngram_fd.tabulate(2))