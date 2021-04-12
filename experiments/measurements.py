from statistics import mean


class Measurements:

    def get_scores(self, sentiment_intensity_analyzer, tokenized_word_list):
        scores = [
            sentiment_intensity_analyzer.polarity_scores(token)["compound"]
            for token in tokenized_word_list
        ]
        return scores, mean(scores)

    def get_sentiment(self, score):
        if score < 0:
            return "neg"
        elif score > 0:
            return "pos"
        else:
            return "neu"
