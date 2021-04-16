import os
from pathlib import Path

from datapreprocessing.preprocessing.Preprocessing import get_corpus, plain_text_corpus, get_words_corpus

data_path_parent = Path(os.path.dirname(__file__)).parent.parent
data_path_corpus = os.path.join(data_path_parent, 'corpus_tweets')

if __name__ == "__main__":
    corpus = get_corpus(data_path_corpus=data_path_corpus)
    plain_test = plain_text_corpus(corpus=corpus)
    print(plain_test)
    words = get_words_corpus(corpus=corpus)
    print(words)

    for infile in sorted(corpus.fileids()):
        print(infile)  # The fileids of each file.
        print(corpus.raw(infile))
        print(corpus.words(infile))
