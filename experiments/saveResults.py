import csv


def save_results(data_path_write, number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets):
    """
    writes to csv file the number of positive, negative and neutral tweets
    :param data_path_write: path to writing csv file
    :param number_of_positive_tweets: int
    :param number_of_negative_tweets: int
    :param number_of_neutral_tweets: int
    :return: None
    """
    pos_tweets = ['number_of_positive_tweets', number_of_positive_tweets]
    neg_tweets = ['number_of_negative_tweets', number_of_negative_tweets]
    neu_tweets = ['number_of_neutral_tweets', number_of_neutral_tweets]
    with open(data_path_write, 'w', newline='', encoding='utf-8') as preprocessed_csv_file:
        writer = csv.writer(preprocessed_csv_file, delimiter='\t')
        writer.writerow(pos_tweets)
        writer.writerow(neg_tweets)
        writer.writerow(neu_tweets)


def get_results(data_path):
    """
    returns number of positive, negative and neutral tweets out of a csv file for plotting
    :param data_path: path to csv file
    :return: number of positive, negative and neutral tweets
    """
    number_of_positive_tweets = -1
    number_of_negative_tweets = -1
    number_of_neutral_tweets = -1
    line_counter = 0

    try:
        with open(data_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            for row in csv_reader:
                if line_counter == 0:
                    number_of_positive_tweets = row[1]
                elif line_counter == 1:
                    number_of_negative_tweets = row[1]
                elif line_counter == 2:
                    number_of_neutral_tweets = row[1]
                line_counter += 1
    except IndexError:
        print("\033[32mArray index out of bounds", "\033[0m")

    if number_of_positive_tweets == -1 or number_of_negative_tweets == -1 or number_of_neutral_tweets == -1:
        print("\033[32mSomething went wrong by reading csv. Wrong format of csv?", "\033[0m")

    return number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets
