import os
from pathlib import Path
import nltk

from experiments.classification import run_sia_classifier_and_save, run_textblob_classifier_and_save, run_textblobDE_classifier_and_save
from experiments.data_lists import list_of_data_all, list_of_data_english, list_of_data_german, \
    list_of_data_all_popularity, list_of_data_english_popularity, list_of_data_german_popularity
from experiments.result_lists import list_of_results_all, list_of_results_english, list_of_results_german, \
    list_of_results_all_popularity, list_of_results_english_popularity, list_of_results_german_popularity
from experiments.plotting import plot_results


data_path_parent = Path(os.path.dirname(__file__)).parent
data_path_save = os.path.join(data_path_parent, 'TwitterProject\\experiments\\results\\')

if __name__ == "__main__":
    nltk.download()

    ###### preprocessing #####

    ##### experiments #####

    # experiment 1
    # sia classifier, all tweets
    run_sia_classifier_and_save(data_path_parent, data_path_save, list_of_data_all, list_of_results_all)

    # experiment 2
    # textblob en classifier, all tweets
    run_textblob_classifier_and_save(data_path_parent, data_path_save, list_of_data_english, list_of_results_english)

    # experiment 3
    # textblob de classifier, all tweets
    run_textblobDE_classifier_and_save(data_path_parent, data_path_save, list_of_data_german, list_of_results_german)

    # experiment 4
    # sia classifier, popular tweets
    run_sia_classifier_and_save(data_path_parent, data_path_save, list_of_data_all_popularity, list_of_results_all_popularity)

    # experiment 5
    # textblob en classifier, popular tweets
    run_textblob_classifier_and_save(data_path_parent, data_path_save, list_of_data_english_popularity, list_of_results_english_popularity)

    # experiment 6
    # textblob de classifier, popular tweets
    run_textblobDE_classifier_and_save(data_path_parent, data_path_save, list_of_data_german_popularity, list_of_results_german_popularity)


    ##### plotting #####
    # experiment 1
    plot_results(list_of_results_all, data_path_save)

    # experiment 2, 3
    list_of_results_textblob = list_of_results_english + list_of_results_german
    plot_results(list_of_results_textblob, data_path_save)

    # experiment 4
    plot_results(list_of_results_all_popularity, data_path_save)

    # experiment 5, 6
    list_of_results_textblob_popularity = list_of_results_english_popularity + list_of_results_german_popularity
    plot_results(list_of_results_textblob_popularity, data_path_save)
