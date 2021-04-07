import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
from statistics import mean

# pretrained sentiment analyzer VADER
# VADER --> for social media, like short sentences with some slang and abbreviations

sia = SentimentIntensityAnalyzer()
# different scores, pos, neg, neu 0-1, compound -1 - 1
print(sia.polarity_scores("Wow, NLTK is really powerful!"))

tweets = [t.replace("://", "//") for t in nltk.corpus.twitter_samples.strings()]


def is_positive(tweet: str) -> bool:
    """True if tweet has positive compound sentiment, False otherwise."""
    return sia.polarity_scores(tweet)["compound"] > 0


shuffle(tweets)
for tweet in tweets[:10]:
    print(">", is_positive(tweet), tweet)

positive_review_ids = nltk.corpus.movie_reviews.fileids(categories=["pos"])
negative_review_ids = nltk.corpus.movie_reviews.fileids(categories=["neg"])
all_review_ids = positive_review_ids + negative_review_ids


def is_positive(review_id: str) -> bool:
    """True if the average of all sentence compound scores is positive."""
    text = nltk.corpus.movie_reviews.raw(review_id)
    scores = [
        sia.polarity_scores(sentence)["compound"]
        for sentence in nltk.sent_tokenize(text)
    ]
    return mean(scores) > 0


shuffle(all_review_ids)
correct = 0
for review_id in all_review_ids:
    if is_positive(review_id):
        if review in positive_review_ids:
            correct += 1
    else:
        if review in negative_review_ids:
            correct += 1

print(F"{correct / len(all_review_ids):.2%} correct")
