import os
from pathlib import Path

from Preprocessing import Preprocessing

data_path_parent = Path(os.path.dirname(__file__)).parent.parent
data_path_corpus = os.path.join(data_path_parent, 'corpus_tweets')

if __name__ == "__main__":
    preprocessing = Preprocessing()
    corpus = Preprocessing.get_corpus(self=preprocessing, data_path_corpus=data_path_corpus)
    plain_test = Preprocessing.plain_text_corpus(self=preprocessing, corpus=corpus)
    print(plain_test)
    words = Preprocessing.get_words_corpus(self=preprocessing, corpus=corpus)
    print(words)

    for infile in sorted(corpus.fileids()):
        print(infile)  # The fileids of each file.
        print(corpus.raw(infile))
        print(corpus.words(infile))
