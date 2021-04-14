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

    def update_number_of_sentiment_lists(self, compound, number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets):
        if compound >= 0.5:
            number_of_positive_tweets += 1
        elif compound <= -0.5:
            number_of_negative_tweets += 1
        else:
            number_of_neutral_tweets += 1
        return number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets
