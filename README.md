# SocialMedia_Sentiment_Analysis


Project for ID2223, we did sentiment analyse of comments in Twitter and output two different attitudes which are positive and negative.
Hugging face: https://huggingface.co/spaces/PatrickML/Twi_sentiment

## How to implement
### Requirements
## Data resource
### Static Data
We use a Twitter Sentiment Dataset from Kaggle -- [Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/datasets/kazanova/sentiment140).

It contains 1,600,000 tweets extracted using the twitter api . The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment 

### Dynamic Data
We wanted to use the Twitter API to get data updated initially, but it doesn't provide the function of extracting tweets free of charge anymore. So we use the Twitter Scraper website [APIFY](https://console.apify.com/) to extract some tweets as our dynamically updated data resource. Since APIFY provides data without sentiment label, we utilized a tool [VADER-Sentiment-Analysis](https://github.com/cjhutto/vaderSentiment) to generate lables of tweets, which fit it into the supervised learning.
