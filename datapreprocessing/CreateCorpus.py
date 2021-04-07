import csv


class CreateCorpus:

    # index 10 for tweet
    def create_text_list(self, data_path_read, index_tweet=10):
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
