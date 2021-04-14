import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import TweetTokenizer
from nltk import tokenize

class Preprocessing:

    def get_corpus(self, data_path_corpus):
        # Create a new corpus by specifying the parameters
        # (1) directory of the new corpus
        # (2) the fileids of the corpus
        # NOTE: in this case the fileids are simply the filenames.

        if data_path_corpus not in nltk.data.path:
            nltk.data.path.append(data_path_corpus)

        corpus = PlaintextCorpusReader(data_path_corpus, '.*')
        return corpus

    def plain_text_corpus(self, corpus):
        # Access the plaintext; outputs pure string/basestring.
        return corpus.raw().strip()

    def get_words_corpus(self, corpus):
        # isalpha = no punctuation words
        words = [w for w in corpus.words() if w.isalpha()]
        # remove stop words like “of,” “a,” “the,”
        stopwords = nltk.corpus.stopwords.words("english")
        words = [w for w in words if w.lower() not in stopwords]
        return words

    def tweets_tokenize_words(self, string):
        tknzr = TweetTokenizer()
        tokenized_word_list = tknzr.tokenize(string)
        return tokenized_word_list

    def get_words_clean(self, tokenized_word_list):
        # remove punctuation + stopwords
        words_cleaned_up = [w for w in tokenized_word_list if w.isalpha() or w.startswith('#')]
        # remove stop words like “of,” “a,” “the,”
        stopwords = nltk.corpus.stopwords.words("english")
        words_cleaned_up = [w for w in words_cleaned_up if w.lower() not in stopwords]
        return words_cleaned_up

    def tweets_tokenize_sentences(self, tweet):
        lines_list = tokenize.sent_tokenize(tweet)
        return lines_list