import csv
import os
import re


# for sorting
def natural_key(string_):
    """
    Sorts like a human, so e.g. not like this: text1, text11, text2 and instead like this text1, text2, text11
    See https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
    """
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]


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

# not used
def create_corpus_directory(data_path_parent, corpus_list):
    """
    creates a directory with textfiles for each tweets
    :param data_path_parent: directory where the folder for the corpus should be created
    :param corpus_list: list of tweets as strings
    :return: the path of the created directory
    """
    # Make new dir for the corpus.
    corpusdir = os.path.join(data_path_parent, 'corpus_tweets/')
    if not os.path.isdir(corpusdir):
        os.mkdir(corpusdir)

    # Output the files into the directory.
    filename = 0
    for text in corpus_list:
        filename += 1
        with open(corpusdir + 'tweet' + str(filename) + '.txt', 'w', encoding='utf-8') as file_out:
            file_out.write(text)

    print(f'Created corpus in directory: {corpusdir}')

    # Check that our corpus do exist and the files are correct.
    assert os.path.isdir(corpusdir)
    for infile, text in zip(sorted(os.listdir(corpusdir), key=natural_key), corpus_list):
        assert open(corpusdir + infile, 'r', encoding='utf-8').read().strip() == text.strip()

    print('Checked corpus successfully.')
    return corpusdir


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