# SocialMedia_Sentiment_Analysis


Project for ID2223, we did sentiment analyse of comments in Twitter and output two different attitudes which are positive and negative.

## Data resource
### Static Data
We use the large amount of Twitter Sentiment Dataset from Kaggle. (Sentiment140 dataset with 1.6 million tweets)[https://www.kaggle.com/datasets/kazanova/sentiment140]
### Dynamic Data
Since we wanted to use twitter api to get data updated initially, but it is not free to got fresh comments freely, we use ____ to crawl historic data for our new feature input resource. We use a tool called "SentimentIntensityAnalyzer" to generate lables of comments in twitter, thus fit it into supervised learning.
