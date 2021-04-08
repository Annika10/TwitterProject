from statistics import mean


class Measurements:

    def get_scores(self, sentiment_intensity_analyzer, tokenized_word_list):
        scores = [
            sentiment_intensity_analyzer.polarity_scores(token)["compound"]
            for token in tokenized_word_list
        ]
        return scores, mean(scores)
