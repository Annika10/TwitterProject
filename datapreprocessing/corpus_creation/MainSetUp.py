import os
from pathlib import Path
import csv

from RemoveOtherLanguages import RemoveOtherLanguages
from CreateCorpus import CreateCorpus

data_path_parent = Path(os.path.dirname(__file__)).parent.parent
#data_path_original = os.path.join(data_path_parent, 'data_corona_15_03_en\\corona_15.3.2020.csv')
#data_path_clean_up = os.path.join(data_path_parent, 'data_corona_15_03_de\\corona_15.3.2020_cleaned_de.csv')


def print_csv(data_path):
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


if __name__ == "__main__":
    # print_csv(data_path=data_path_original)
    remover = RemoveOtherLanguages()
    RemoveOtherLanguages.remove(
        self=remover, data_path_read=data_path_original, data_path_write=data_path_clean_up, language="en")
    corpus_object = CreateCorpus()
    corpus_text_list = CreateCorpus.create_text_list(self=corpus_object, data_path_read=data_path_clean_up)
    corpusdir = CreateCorpus.create_corpus_directory(
        self=corpus_object, data_path_parent=data_path_parent, corpus_list=corpus_text_list)