import os
from pathlib import Path
import csv

from RemoveOtherLanguages import RemoveOtherLanguages
from CreateCorpus import CreateCorpus

parentPath = Path(os.path.dirname(__file__)).parent
data_path_original = os.path.join(parentPath, 'data_march2020\\14dayquarantine.csv')
data_path_preprocessed = os.path.join(parentPath, 'data_march2020\\14dayquarantine_preprocessed.csv')


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
    print_csv(data_path=data_path_original)
    remover = RemoveOtherLanguages()
    RemoveOtherLanguages.remove(self=remover, data_path_read=data_path_original, data_path_write=data_path_preprocessed)
    corpus = CreateCorpus()
    corpus_text_list = CreateCorpus.create_text_list(self=corpus, data_path_read=data_path_preprocessed)
