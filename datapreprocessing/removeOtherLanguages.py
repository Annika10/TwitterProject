import csv


class removeOtherLanguages:

    # index 11 for language
    # TODO
    def remove(self, data_path):
        with open(data_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    for index in range(len(row)):
                        if index == 11 and (row[index] != "en" and row[index] != "und"):
                            print("index", index, row[index], end="\t")
                    line_count += 1
                    print()
            print(f'Processed {line_count} lines.')
            pass