import os
from pathlib import Path
from statistics import mean
from nltk.sentiment import SentimentIntensityAnalyzer

from datapreprocessing.preprocessing.Preprocessing import Preprocessing
from experiments.measurements import Measurements

data_path_parent = Path(os.path.dirname(__file__)).parent
data_path_corpus = os.path.join(data_path_parent, 'corpus_tweets')

if __name__ == "__main__":
    preprocessing = Preprocessing()
    corpus = Preprocessing.get_corpus(self=preprocessing, data_path_corpus=data_path_corpus)
    plain_text_corpus = Preprocessing.plain_text_corpus(self=preprocessing, corpus=corpus)
    words_corpus = Preprocessing.get_words_corpus(self=preprocessing, corpus=corpus)

    sia = SentimentIntensityAnalyzer()
    measurements = Measurements()

    for infile in sorted(corpus.fileids()):
        print(infile)
        text = corpus.raw(infile)
        print(text)

        tokenized_word_list = Preprocessing.tweets_tokenize_words(self=preprocessing, string=text)
        print(tokenized_word_list)

        scores, mean_score = Measurements.get_scores(self=measurements, sentiment_intensity_analyzer=sia, tokenized_word_list=tokenized_word_list)
        print(scores, mean_score)

        words_cleaned_up = Preprocessing.get_words_clean(self=preprocessing, tokenized_word_list=tokenized_word_list)
        print(words_cleaned_up)

        scores1, mean_score1 = Measurements.get_scores(self=measurements, sentiment_intensity_analyzer=sia,
                                                     tokenized_word_list=words_cleaned_up)
        print(scores1, mean_score1)

