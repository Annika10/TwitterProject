from statistics import mean


class Measurements:

    def get_scores(self, sentiment_intensity_analyzer, tokenized_word_list):
        """
        returns scores and mean scores of a tokenized word list
        :param sentiment_intensity_analyzer: an object of an sentiment analyzer
        :param tokenized_word_list: a list of words
        :return: scores, mean from scores
        """
        scores = [
            sentiment_intensity_analyzer.polarity_scores(token)["compound"]
            for token in tokenized_word_list
        ]
        return scores, mean(scores)

    def update_number_of_sentiment_lists(self, compound, number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets):
        """
        updates the given lists of number of sentiments tweets
        :param compound: calculated compound of the sentiment analyzer
        :param number_of_positive_tweets: number of positive tweets until now
        :param number_of_negative_tweets: number of negative tweets until now
        :param number_of_neutral_tweets: number of neutral tweets until now
        :return: updated numbers of positive, negative and neutral tweets
        """
        if compound >= 0.5:
            number_of_positive_tweets += 1
        elif compound <= -0.5:
            number_of_negative_tweets += 1
        else:
            number_of_neutral_tweets += 1
        return number_of_positive_tweets, number_of_negative_tweets, number_of_neutral_tweets
