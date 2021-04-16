import os
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

from datapreprocessing.preprocessing.Preprocessing import get_corpus, plain_text_corpus, get_words_corpus, tweets_tokenize_words, get_words_clean
from experiments.measurements import get_scores

data_path_parent = Path(os.path.dirname(__file__)).parent
data_path_corpus = os.path.join(data_path_parent, 'corpus_tweets')

if __name__ == "__main__":
    corpus = get_corpus(data_path_corpus=data_path_corpus)
    plain_text_corpus = plain_text_corpus(corpus=corpus)
    words_corpus = get_words_corpus(corpus=corpus)

    sia = SentimentIntensityAnalyzer()

    for infile in sorted(corpus.fileids()):
        print(infile)
        text = corpus.raw(infile)
        print(text)

        tokenized_word_list = tweets_tokenize_words(string=text)
        print(tokenized_word_list)

        scores, mean_score = get_scores(sentiment_intensity_analyzer=sia, tokenized_word_list=tokenized_word_list)
        print(scores, mean_score)

        words_cleaned_up = get_words_clean(tokenized_word_list=tokenized_word_list)
        print(words_cleaned_up)

        scores1, mean_score1 = get_scores(sentiment_intensity_analyzer=sia,
                                                     tokenized_word_list=words_cleaned_up)
        print(scores1, mean_score1)

