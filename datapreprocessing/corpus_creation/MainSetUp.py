import os
from pathlib import Path

from datapreprocessing.corpus_creation.CreateCorpus import create_text_list, create_corpus_directory, remove, print_csv

data_path_parent = Path(os.path.dirname(__file__)).parent.parent
list_of_data_original = [
    'data_corona_15_03_en\\corona_15.3.2021.csv',
    'data_corona_15_03_en\\corona_15.3.2020.csv',
    'data_corona_15_03_de\\corona_15.3.2021.csv',
    'data_corona_15_03_de\\corona_15.3.2020.csv'
]
list_of_results_cleaned_up = [
    'data_corona_15_03_en\\corona_15.3.2021_cleaned_en.csv',
    'data_corona_15_03_en\\corona_15.3.2020_cleaned_en.csv',
    'data_corona_15_03_de\\corona_15.3.2021_cleaned_de.csv',
    'data_corona_15_03_de\\corona_15.3.2020_cleaned_de.csv'
]


if __name__ == "__main__":

    for index in range(len(list_of_data_original)):
        data_path_read = os.path.join(data_path_parent, list_of_data_original[index])
        data_path_write = os.path.join(data_path_parent, list_of_results_cleaned_up[index])
        remove(data_path_read, data_path_write)
        print_csv(data_path_write)
        tweet_text_list = create_text_list(data_path_write)
        # corpusdir = create_corpus_directory(data_path_parent, tweet_text_list)
