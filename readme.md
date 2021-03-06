# Project Intelligent Information Systems
This project is implemented as a student project of the course Intelligent Information Systems.
The aim is to compare the sentiment of tweets from the 15.03.2020 and 15.03.2021 which deal with the covid-19 crisis. 
For this I downloaded the corresponding tweets and used two pretrained classifiers for gaining the sentiment.
In the end the results are compared by plotting them in a pie chart.
My hypothesis is that the tweets are getting more negative sentiment in 2021 because the covid-19 crisis takes already a year.
Important: the data set couldn't be uploaded due to its size. 

# Scraping Tweets
For scraping the tweets of the 15.03.2020 and 15.03.2021 I use the tool [Twint](https://github.com/twintproject/twint).
With Twint I scrape multiple metadata. 
The following metadata of every tweet are considered:

- id: id of tweet	
- created_at: timestamp of creation of tweet (e.g. 2020-03-15 16:05:20 Central European Time)	
- date: here 15.03.2020	
- time: e.g. 16:05:20 			
- tweet: the actual tweet	
- language: language prefix (e.g. "en" for English)	
- replies_count: number of replies to this tweet	
- retweets_count: number of retweets of this tweet
- likes_count: number of likes of this tweet

I search for all tweets which include the term: "corona".

Note that the scraping tool Twint uses the Western European Time, but I save them in the Central European Time.
Therefore, the hour at 15.3. from 0:00 to 1:00 doesn't occur in my dataset but on the other hand the hour from 0:00 to 1:00 at 16.3.
The scraping is implemented in [twint_search.py](./twint_search/twint_search.py).
The scraped data can be found in the folders [data_corona_15_03_en](./data_corona_15_03_en) and [data_corona_15_03_de](./data_corona_15_03_de).
In the first run I wanted to scrape all tweets of march with terms which belong to the covid-19 crisis, but this was way too much data and my computer couldn’t handle this. 
The scraping is done in [twint_search.py](twint_search/twint_search.py).

## Problems by Scraping
Unfortunately, the tool [Twint](https://github.com/twintproject/twint) doesn't work properly. 
I defined that only English tweets should be scraped, but the tool doesn't take this into account and scraped all tweets.
Therefore, I had to preprocess the scraped data and implement a function which sorts out the non-English tweets.
Therefore, I also consider German tweets in my analysis because I can get them easily by sorting out all non-German tweets.

## Popular tweets

For reflecting more the overall opinion and not only some individual opinions, I made a selection on the tweets. 
The selection is named popular tweets. 
I refer a tweet as popular when it has at least 100 replies, retweets or likes. 

## Resulting Dataset
The following table shows the number of tweets and popular tweets for each language at 15.3.2020. 

| | all tweets | popular tweets |
--- | --- | ---
|English tweets|210 502|1 869|
|German tweets|29 961|509|

The following table shows the number of tweets and popular tweets for each language at 15.3.2021. 

| | all tweets | popular tweets |
--- | --- | ---
|English tweets|10 845|101|
|German tweets|17 252|261|

As you will notice there are a lot more tweets related to "corona" at 15.03.2020 than at 15.03.2021. 
Especially the tweets in English drop down from 210502 to 10845 tweets.
I assume that this is due to the point that the corona crisis just started in March 2020 in the English and German speaking countries and therefore more people spoke about it these times.  

# Experiments

In each experiment I run through each tweet and calculate the polarity score also known as compound of each tweet.
I consider experiments with all selected tweets as well as a selection of popular tweets.
A tweet is considered as positive, neutral or negative by the following polarity scores. 

    positive sentiment: polarity score >= 0.05
    neutral sentiment:  polarity score < 0.05 and polarity score > -0.05 
    negative sentiment: polarity score <= -0.05

The experiments with its preprocessing and plotting is implemented in [main.py](main.py).

## Preprocessing

As preprocessing we collect the tweets which are in English and German language.
In addition, we select from these tweets the popular tweets which are defined like explained above. 

## Running Experiments
    
For calculating the polarity score I use two different text processing libraries, the [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer) of the [nltk](https://www.nltk.org/) library and the [TextBlob](https://textblob.readthedocs.io/en/dev/) of the textblob library. 
In addition, I use the German version of the [textblob](https://textblob-de.readthedocs.io/en/latest/) library for processing the German tweets. 
With this polarity score I determine for each tweet, if it is a positive, negative or neutral tweet. 
In the end I save the number of positive, negative and neutral tweets in the [results folder](experiments/results).

## Result plotting

The number of positive, negative and neutral tweets are plotted as pie diagrams with [matplotlib](https://matplotlib.org/).
The first row shows the pie charts for English tweets for 15.03.2020 and 15.03.2021.
The second row shows the same for German tweets. 
Each chart shows the percentage of each category of tweets. 
The neutral tweets are colored green, the positive tweets blue and the negative tweets orange.
In each title of the pie chart is the overall number of collected tweets.  

## Experiment 1
### Sentiment Intensity Analyzer - all tweets

In the first experiment I use the [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer) of the [nltk](https://www.nltk.org/) library.
The sentiment analyzer is run over all tweets of the 15.03.2020 and 15.03.2021.
The results of these numbers are shown in the following image. 
![Alt text](result_images/experiment1.png "sia")

## Experiment 2 and Experiment 3
### Textblob - all tweets

In the second experiment I use [TextBlob](https://textblob.readthedocs.io/en/dev/) for the text processing library.
Note that the third experiment is similar to the second but uses [TextBlob for German language](https://textblob-de.readthedocs.io/en/latest/) which is its own library and not included in the standard textblob library. 
The results are shown in the following.
![Alt text](result_images/experiment2_3.png "test blob")

## Experiment 4
### Sentiment Intensity Analyzer - popular tweets

The structure of the fourth experiment is equal to the structure of the first experiment.
The difference is the used data. 
In this experiment only popular tweets (more than 100 retweets, replies or likes) are considered. 
![Alt text](result_images/experiment4.png "sia high popularity")

## Experiment 5 and Experiment 6
### Textblob - popular tweets

The fifth and sixth experiment is the same as the second and third experiment, but the input data are popular tweets like in experiment four.
![Alt text](result_images/experiment5_6.png "high popularity")

## Analysis of experiments
Firstly, I compare the differences between both sentiment analyzers. 
By comparing with the results of all tweets I noticed that though the number of positive tweets for English tweet are very similar, the [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer) of the [nltk](https://www.nltk.org/) library declares more English tweets as negative. 
By comparing the sentiment of German tweets, the differences are bigger. 
The [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer) detects way more negative German tweets but way fewer positive tweets than the [TextBlob](https://textblob.readthedocs.io/en/dev/) analyzer. 
I can see the same schema by comparing the results of high popular tweets.

When comparing the differences of sentiment in tweets which are in English or German language, I draw the conclusion that the relative number of positive, negative and neutral tweets doesn’t really differ by using the [TextBlob](https://textblob.readthedocs.io/en/dev/) analyzer. 
By looking at the [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentimentintensityanalyzer#nltk.sentiment.vader.SentimentIntensityAnalyzer) you can see that the relative number of negative tweets for English and German tweets are quite similar, but the English tweets have more positive tweets, in detail about 35% positive tweets in comparison to 3-4% positive tweets in German. 

Unfortunately, I cannot see any differences in the sentiment in the years 2020 and 2021. 
In addition, there aren’t huge differences in the percentages by considering all tweets or high popular tweets.

# Conclusion

My hypothesis that the tweets are getting a more negative sentiment in 2021 in comparison to 2020 is not fulfilled. 
By using two sentiment analyzers I cannot see this behavior for 2020 and 2021. 
It seems that the sentiment and public opinion about the covid-19 crisis didn’t change that much by analyzing tweets. 

## Why is this project an intellgent information system?
This project is an intelligent information system because it fulfills the most important functionalities of an intelligent information system. 
It stores information and knowledge in form of csv files where information (here tweets) are stored and with pie charts which show knowledge. 
It answers the question if the sentiment and public opinion about the covid-19 crisis changes from March 2020 to March 2021 in German and English-speaking countries and it discovers knowledge by drawing conclusions about this opinion.

## Future work
I noticed that most of the English-speaking medias speak about the covid-19 crisis and not the corona crisis whereas in Germany most medias call it corona crisis.
Because of my background of living in Germany I scraped tweets with the term "corona" in it. 
Maybe there would be more especially English tweets if I instead scraped tweets with the term "covid" in it.  
