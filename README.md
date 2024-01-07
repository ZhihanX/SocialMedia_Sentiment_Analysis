# SocialMedia_Sentiment_Analysis


Project for ID2223, we did a sentiment analysis of comments on Twitter and output two different attitudes which are positive and negative.

Hugging face:

App: https://huggingface.co/spaces/PatrickML/Twi_sentiment 

Monitor: https://huggingface.co/spaces/PatrickML/Twi_sentiment_monitor

## 1. Overview
![Whole Pipeline](https://github.com/ZhihanX/SocialMedia_Sentiment_Analysis/blob/main/pipeline.png)
## 2. How to implement
All the .ipynb files can directly execute with the Colab. The .py files should be settled locally, and the project names which match your Hopsworks or Modal account should be modified.
### Requirements
```
#If you have windows, install twofish
twofish
hopsworks
joblib
scikit-learn==1.1.1
seaborn
dataframe-image
modal
gradio==3.14
vaderSentiment
```
### Download Dataset
Download the [Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/datasets/kazanova/sentiment140) (a .csv file) from Kaggle, and save in Google Drive with the directory: '/content/drive/MyDrive/twitter_dataset/training.1600000.processed.noemoticon.csv'.
## 3. Data resource
### Static Data
We use a Twitter Sentiment Dataset from Kaggle -- [Sentiment140 dataset with 1.6 million tweets](https://www.kaggle.com/datasets/kazanova/sentiment140).

It contains 1,600,000 tweets extracted using the Twitter API. The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment 

### Dynamic Data
We wanted to use the Twitter API to get data updated initially, but it doesn't provide the function of extracting tweets free of charge anymore. So we use the Twitter Scraper website [APIFY](https://console.apify.com/) to extract some tweets as our dynamically updated data resource. Since APIFY provides data without sentiment label, we utilized a tool [VADER-Sentiment-Analysis](https://github.com/cjhutto/vaderSentiment) to generate lables of tweets, which fit it into the supervised learning.

## 4. Procedure
1. twitter_backfill.ipynb
   
   In this file, we do preprocessing on the static dataset from Kaggle. We also analyze the data to see its distribution and also generate the word cloud figures. After the processing, the feature is uploaded to the Hopsworks.
   
2. dynamic_feature_pipeline.ipynb

   In this file, we do preprocessing on the dynamic dataset from Apify. As these data are unlabeled, we use VADER-Sentiment-Analysis tool to label the data.

   The tool outputs a sentiment score:
   ```
   Less than or equal to 0: Negative --- 0
   Greater than 0: Positive --- 1
   ```
    After the processing, the feature is uploaded to the Hopsworks.
   
3. dynamic_update.py

   Get the dynamic feature from Hopsworks. Set a yearly updating Modal function which will add the dynamic data once a year to the whole dataset (mentioned in step 1.).
4. twitter_training_pipeline.ipynb

   Get the whole dataset and feature from Hopsworks to train a model. We use the TfidfVectorizer to convert the text data into features, ngram_range=(1,2) which means unigram or bigram. We compared 3 different approaches, BernoulliNB, C-Support Vector, and Logistic Regression, and finally chose Logistic Regression because it has the best performance. After training and evaluating, we upload the LR model and the vectoriser generated in TfidfVectorizer.

5. twitter_batch_pipeline.py

   The batch pipeline is to infer with the generated model in step 4. The prediction results and the logs are saved into Hopsworks.
