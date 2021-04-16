import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import TweetTokenizer
from nltk import tokenize


def get_corpus(data_path_corpus):
    """
    creates a nltk plain text corpus reader element
    :param data_path_corpus: path to corpus out of textfiles for each tweets
    :return: object of nltk plain text corpus reader
    """

    if data_path_corpus not in nltk.data.path:
        nltk.data.path.append(data_path_corpus)

    corpus = PlaintextCorpusReader(data_path_corpus, '.*')
    return corpus


def plain_text_corpus(corpus):
    """
    returns the plaintext (string) of the whole corpus
    :param corpus: corpus object
    :return: plaintext
    """
    return corpus.raw().strip()


def get_words_corpus(corpus):
    """
    returns list of all words in the corpus + removes punctuation words and stopwords
    :param corpus: corpus object
    :return: list of adjusted words
    """
    # isalpha = no punctuation words
    words = [w for w in corpus.words() if w.isalpha()]
    # remove stop words like “of,” “a,” “the,”
    stopwords = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w.lower() not in stopwords]
    return words


def tweets_tokenize_words(tweet):
    """
    tokenizes a tweet into words
    :param tweet: tweet
    :return: list of tokenized tweet
    """
    tknzr = TweetTokenizer()
    tokenized_word_list = tknzr.tokenize(tweet)
    return tokenized_word_list


def get_words_clean(tokenized_word_list):
    """
    cleans up a tokenized tweet stored in a list
    :param tokenized_word_list: list of tokenized tweet
    :return: cleanup of tokenized tweet
    """
    # remove punctuation + stopwords, exclude # because hashtags should be considered
    words_cleaned_up = [w for w in tokenized_word_list if w.isalpha() or w.startswith('#')]
    # remove stop words like “of,” “a,” “the,”
    stopwords = nltk.corpus.stopwords.words("english")
    words_cleaned_up = [w for w in words_cleaned_up if w.lower() not in stopwords]
    return words_cleaned_up


def tweets_tokenize_sentences(tweet):
    """
    tokenize tweet into sentences
    :param tweet: string
    :return: list of sentences
    """
    lines_list = tokenize.sent_tokenize(tweet)
    return lines_list
