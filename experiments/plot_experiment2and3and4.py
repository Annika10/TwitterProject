import matplotlib.pyplot as plt
from pathlib import Path
import os
import numpy as np

from experiments.saveResults import get_results

data_path_parent = Path(os.path.dirname(__file__)).parent
data_path_results = os.path.join(data_path_parent, 'experiments\\results\\')
list_of_results = [
    'corona_15.3.2021_results_en.csv',
    'corona_15.3.2020_results_en.csv',
    'corona_15.3.2021_results_de.csv',
    'corona_15.3.2020_results_de.csv'
]
list_of_results_1 = [
    'corona_15.3.2020_results_en_textblob.csv',
    'corona_15.3.2020_results_de_textblob.csv',
    'corona_15.3.2021_results_en_textblob.csv',
    'corona_15.3.2021_results_de_textblob.csv',
]
list_of_results_2 = [
    'corona_15.3.2021_results_en_textblob_high_popularity.csv',
    'corona_15.3.2020_results_en_textblob_high_popularity.csv',
    'corona_15.3.2021_results_de_textblob_high_popularity.csv',
    'corona_15.3.2020_results_de_textblob_high_popularity.csv',
]
list_of_results_3 = [
    'corona_15.3.2021_results_en_high_popularity.csv',
    'corona_15.3.2020_results_en_high_popularity.csv',
    'corona_15.3.2021_results_de_high_popularity.csv',
    'corona_15.3.2020_results_de_high_popularity.csv',
]
used_list = list_of_results_3

if __name__ == "__main__":

    # create a figure with 4 subplots
    fig, axs = plt.subplots(2, 2)
    label = ["positive tweets", "negative tweets", "neutral tweets"]
    dict_axes = {0: axs[0, 0], 1: axs[0, 1], 2: axs[1, 0], 3: axs[1, 1]}
    dict_names = {0: "2020_en", 1: "2020_de", 2: "2021_en", 3: "2021_de"}

    for index in range(len(used_list)):
        number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = get_results(data_path_results + used_list[index])
        sum_tweets = int(number_of_positive_tweets) + int(number_of_negative_tweets) + int(number_of_neutral_tweets)
        values = np.array([number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets])

        # plot each pie chart in a separate subplot
        dict_axes[index].pie(values, labels=label, autopct='%1.2f%%')
        dict_axes[index].set_title(dict_names[index] + ': ' + str(sum_tweets) + ' tweets')

    plt.show()
