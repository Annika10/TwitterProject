import os
from datapreprocessing.create_dataset import remove, select_tweets_with_high_number_of_reactions


def run_preprocessing(data_path_parent, list_of_data_original, list_of_results_cleaned_up, list_of_results_high_popularity, language='en'):
    for index in range(len(list_of_data_original)):
        data_path_read = os.path.join(data_path_parent, list_of_data_original[index])
        data_path_write = os.path.join(data_path_parent, list_of_results_cleaned_up[index])
        data_path_write_popularity = os.path.join(data_path_parent, list_of_results_high_popularity[index])

        ### select english tweets
        remove(data_path_read, data_path_write, language=language)

        ### select popular tweets
        min_count_reaction = 100
        indexes_reactions = [
            15,  # replies
            16,  # retweets
            17  # likes
        ]
        select_tweets_with_high_number_of_reactions(data_path_write, data_path_write_popularity, min_count_reaction,
                                                    indexes_reactions)