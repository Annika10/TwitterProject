from textblob import TextBlob
import os
from pathlib import Path

from datapreprocessing.corpus_creation.CreateCorpus import create_text_list
from experiments.measurements import update_number_of_sentiment_lists
from experiments.saveResults import save_results

data_path_parent = Path(os.path.dirname(__file__)).parent

list_of_data = [
    'data_corona_15_03_en\\corona_15.3.2021_cleaned_en.csv',
    'data_corona_15_03_en\\corona_15.3.2020_cleaned_en.csv',
]
list_of_results = [
    'corona_15.3.2021_results_en_textblob.csv',
    'corona_15.3.2020_results_en_textblob.csv',
]

data_path_save = os.path.join(data_path_parent, 'experiments\\results\\')

if __name__ == "__main__":

    for index in range(len(list_of_data)):
        list_of_tweets = create_text_list(data_path_read=os.path.join(data_path_parent, list_of_data[index]), index_tweet=10)
        number_of_tweets = len(list_of_tweets)
        number_of_positive_tweets = 0
        number_of_negative_tweets = 0
        number_of_neutral_tweets = 0

        for tweet in list_of_tweets:
            print("new tweet")
            print(tweet)
            testimonial = TextBlob(tweet)
            print(testimonial.sentiment.polarity)
            number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = \
                update_number_of_sentiment_lists(
                    compound=testimonial.sentiment.polarity,
                    number_of_positive_tweets=number_of_positive_tweets,
                    number_of_negative_tweets=number_of_negative_tweets,
                    number_of_neutral_tweets=number_of_neutral_tweets
                )

        print("number_of_positive_tweets", number_of_positive_tweets)
        print("number_of_negative_tweets", number_of_negative_tweets)
        print("number_of_neutral_tweets", number_of_neutral_tweets)
        print("number_of_tweets", number_of_tweets)

        if number_of_tweets == (number_of_positive_tweets + number_of_negative_tweets + number_of_neutral_tweets):
            save_results(data_path_save + list_of_results[index], number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets)
        else:
            print("\033[32mSomething went wrong", "\033[0m")