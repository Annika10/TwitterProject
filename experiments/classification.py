import os
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from textblob_de import TextBlobDE as TextBlobDE

from datapreprocessing.create_dataset import create_text_list
from experiments.measurements import update_number_of_sentiment_lists
from experiments.saveResults import save_results


def run_sia_classifier_and_save(data_path_parent, data_path_save, list_of_data, list_of_results):
    """
    count for each tweet it's sentiment and save the numbers in a csv with the nltk sentiment intensity analyzer
    :param data_path_parent: path to parent folder of project
    :param data_path_save: path to folder where results are stored
    :param list_of_data: list with the csv's which are analyzed
    :param list_of_results: list with csv's where the numbers are stored
    :return: None
    """
    sid = SentimentIntensityAnalyzer()

    for index in range(len(list_of_data)):
        list_of_tweets = create_text_list(data_path_read=os.path.join(data_path_parent, list_of_data[index]),
                                          index_tweet=10)
        number_of_tweets = len(list_of_tweets)
        number_of_positive_tweets = 0
        number_of_negative_tweets = 0
        number_of_neutral_tweets = 0

        for tweet in list_of_tweets:
            ss = sid.polarity_scores(tweet)
            number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = \
                update_number_of_sentiment_lists(
                    compound=ss['compound'],
                    number_of_positive_tweets=number_of_positive_tweets,
                    number_of_negative_tweets=number_of_negative_tweets,
                    number_of_neutral_tweets=number_of_neutral_tweets
                )

        if number_of_tweets == (number_of_positive_tweets + number_of_negative_tweets + number_of_neutral_tweets):
            save_results(data_path_save + list_of_results[index], number_of_positive_tweets, number_of_negative_tweets,
                         number_of_neutral_tweets)
        else:
            print("\033[32mSomething went wrong", "\033[0m")


def run_textblob_classifier_and_save(data_path_parent, data_path_save, list_of_data, list_of_results):
    """
    count for each tweet it's sentiment and save the numbers in a csv with the textblob lib
    :param data_path_parent: path to parent folder of project
    :param data_path_save: path to folder where results are stored
    :param list_of_data: list with the csv's which are analyzed
    :param list_of_results: list with csv's where the numbers are stored
    :return: None
    """
    for index in range(len(list_of_data)):
        list_of_tweets = create_text_list(data_path_read=os.path.join(data_path_parent, list_of_data[index]), index_tweet=10)
        number_of_tweets = len(list_of_tweets)
        number_of_positive_tweets = 0
        number_of_negative_tweets = 0
        number_of_neutral_tweets = 0

        for tweet in list_of_tweets:
            testimonial = TextBlob(tweet)
            number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = \
                update_number_of_sentiment_lists(
                    compound=testimonial.sentiment.polarity,
                    number_of_positive_tweets=number_of_positive_tweets,
                    number_of_negative_tweets=number_of_negative_tweets,
                    number_of_neutral_tweets=number_of_neutral_tweets
                )

        if number_of_tweets == (number_of_positive_tweets + number_of_negative_tweets + number_of_neutral_tweets):
            save_results(data_path_save + list_of_results[index], number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets)
        else:
            print("\033[32mSomething went wrong", "\033[0m")


def run_textblobDE_classifier_and_save(data_path_parent, data_path_save, list_of_data, list_of_results):
    """
    count for each tweet it's sentiment and save the numbers in a csv with the textblob lib for german language
    :param data_path_parent: path to parent folder of project
    :param data_path_save: path to folder where results are stored
    :param list_of_data: list with the csv's which are analyzed
    :param list_of_results: list with csv's where the numbers are stored
    :return: None
    """
    for index in range(len(list_of_data)):
        list_of_tweets = create_text_list(data_path_read=os.path.join(data_path_parent, list_of_data[index]), index_tweet=10)
        number_of_tweets = len(list_of_tweets)
        number_of_positive_tweets = 0
        number_of_negative_tweets = 0
        number_of_neutral_tweets = 0

        for tweet in list_of_tweets:
            testimonial = TextBlobDE(tweet)
            number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = \
                update_number_of_sentiment_lists(
                    compound=testimonial.sentiment.polarity,
                    number_of_positive_tweets=number_of_positive_tweets,
                    number_of_negative_tweets=number_of_negative_tweets,
                    number_of_neutral_tweets=number_of_neutral_tweets
                )

        if number_of_tweets == (number_of_positive_tweets + number_of_negative_tweets + number_of_neutral_tweets):
            save_results(data_path_save + list_of_results[index], number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets)
        else:
            print("\033[32mSomething went wrong", "\033[0m")