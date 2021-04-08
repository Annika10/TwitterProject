import csv
import os
import re

class CreateCorpus:


    # for sorting
    def natural_key(self, string_):
        """See https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/"""
        return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

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

    def create_corpus_directory(self, data_path_parent, corpus_list):
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
        for infile, text in zip(sorted(os.listdir(corpusdir), key=self.natural_key), corpus_list):
            assert open(corpusdir + infile, 'r', encoding='utf-8').read().strip() == text.strip()

        print('Checked corpus successfully.')
        return corpusdir
