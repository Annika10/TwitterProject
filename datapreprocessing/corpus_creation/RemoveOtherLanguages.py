import csv


class RemoveOtherLanguages:

    # index 11 for language
    def remove(self, data_path_read, data_path_write, index_language=11, language="en"):
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
