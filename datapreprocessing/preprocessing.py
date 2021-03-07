from removeOtherLanguages import removeOtherLanguages
import os
from pathlib import Path
import csv

parentPath = Path(os.path.dirname(__file__)).parent
data_path = os.path.join(parentPath, 'data_march2020\\14dayquarantine.csv')


def readCsv(data_path):
    with open(data_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                for index in range(len(row)):
                    print("index", index, row[index], end="\t")
                line_count += 1
                print()
        print(f'Processed {line_count} lines.')


if __name__ == "__main__":
    readCsv(data_path=data_path)
    remover = removeOtherLanguages()
    removeOtherLanguages.remove(self=remover, data_path=data_path)
