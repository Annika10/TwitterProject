import matplotlib.pyplot as plt
import numpy as np

from experiments.saveResults import get_results


def plot_results(list_of_results, data_path_results):
    # create a figure with 4 subplots
    fig, axs = plt.subplots(2, 2)
    label = ["positive tweets", "negative tweets", "neutral tweets"]
    dict_axes = {0: axs[0, 0], 1: axs[0, 1], 2: axs[1, 0], 3: axs[1, 1]}
    dict_names = {0: "2020_en", 1: "2020_de", 2: "2021_en", 3: "2021_de"}

    for index in range(len(list_of_results)):
        number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets = get_results(
            data_path_results + list_of_results[index])
        sum_tweets = int(number_of_positive_tweets) + int(number_of_negative_tweets) + int(number_of_neutral_tweets)
        values = np.array([number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets])

        # plot each pie chart in a separate subplot
        dict_axes[index].pie(values, labels=label, autopct='%1.2f%%')
        dict_axes[index].set_title(dict_names[index] + ': ' + str(sum_tweets) + ' tweets')

    plt.show()
