import os
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

from datapreprocessing.corpus_creation.CreateCorpus import CreateCorpus
from datapreprocessing.preprocessing.Preprocessing import Preprocessing
from experiments.measurements import Measurements

data_path_parent = Path(os.path.dirname(__file__)).parent
data_path_read = os.path.join(data_path_parent, 'data_corona_15_03_en\\corona_15.3.2021_cleaned_en.csv')

if __name__ == "__main__":
    corpus = CreateCorpus()
    preprocessing = Preprocessing()
    sid = SentimentIntensityAnalyzer()
    measurements = Measurements()

    list_of_tweets = corpus.create_text_list(data_path_read=data_path_read, index_tweet=10)
    number_of_tweets = len(list_of_tweets)
    number_of_positive_tweets = 0
    number_of_negative_tweets = 0
    number_of_neutral_tweets = 0

    for tweet in list_of_tweets:
        print("new tweet")
        sentences_list = preprocessing.tweets_tokenize_sentences(tweet=tweet)
        for sentence in sentences_list:
            print(sentence)
            ss = sid.polarity_scores(sentence)
            for k in sorted(ss):
                print('{0}: {1}, '.format(k, ss[k]), end='')
            print()
            number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = \
                measurements.update_number_of_sentiment_lists(
                    compound=ss['compound'],
                    number_of_positive_tweets=number_of_positive_tweets,
                    number_of_negative_tweets=number_of_negative_tweets,
                    number_of_neutral_tweets=number_of_neutral_tweets
                )

    print("number_of_positive_tweets", number_of_positive_tweets)
    print("number_of_negative_tweets", number_of_negative_tweets)
    print("number_of_neutral_tweets", number_of_neutral_tweets)
    print("number_of_tweets", number_of_tweets)
