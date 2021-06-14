import csv


# index 10 for tweet
def create_text_list(data_path_read, index_tweet=10):
    """
    creates a list of all tweets as elements
    :param data_path_read: path to read in the csv with tweets
    :param index_tweet: index in the csv file where the tweets are stored
    :return: list with all tweets
    """
    with open(data_path_read, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        corpus_list = list()
        for row in csv_reader:
            if not line_count == 0:
                corpus_list.append(str(row[index_tweet]))
            line_count += 1

    print(f'Processed {line_count} lines and the corpus list consists of {len(corpus_list)} elements.')
    return corpus_list


# index 11 for language
def remove(data_path_read, data_path_write, index_language=11, language="en"):
    """
    removes the lines which aren't in the required language or in undefined language
    :param data_path_read: path to csv from which we read (all tweets)
    :param data_path_write: path to csv where tweets in required languages are stored
    :param index_language: index in the csv file where the language is defined
    :param language: prefix of required language
    :return: None
    """
    with open(data_path_read, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        line_count_en = 0
        with open(data_path_write, 'w', newline='', encoding='utf-8') as preprocessed_csv_file:
            writer = csv.writer(preprocessed_csv_file, delimiter='\t')
            for row in csv_reader:
                if line_count == 0:
                    writer.writerow(row)
                    line_count_en += 1
                else:
                    if row[index_language] == language or row[index_language] == "und":
                        writer.writerow(row)
                        line_count_en += 1
                line_count += 1

        print(f'Processed {line_count} lines. Remaining lines: {line_count_en}')


def print_csv(data_path):
    """
    function for printing each row of a csv file
    :param data_path: path to csv file
    :return: None
    """
    with open(data_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                for index in range(len(row)):
                    print(index, ":", row[index], end="\t")
                line_count += 1
                print()
        print(f'Processed {line_count} lines.')


def select_tweets_with_high_number_of_reactions(data_path_read, data_path_write, min_count_reaction, indexes_reaction):
    """
    # TODO
    :param data_path_read:
    :param data_path_write:
    :param min_count_reaction:
    :param indexes_reaction:
    :return:
    """
    with open(data_path_read, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        line_count_popular = 0
        with open(data_path_write, 'w', newline='', encoding='utf-8') as preprocessed_csv_file:
            writer = csv.writer(preprocessed_csv_file, delimiter='\t')
            for row in csv_reader:
                if line_count == 0:
                    writer.writerow(row)
                    line_count_popular += 1
                else:
                    # TODO: fix duplicates
                    for index_reaction in indexes_reaction:
                        if int(row[index_reaction]) >= min_count_reaction:
                            writer.writerow(row)
                            line_count_popular += 1
                            break
                line_count += 1

        print(f'Processed {line_count} lines. Remaining lines: {line_count_popular}')