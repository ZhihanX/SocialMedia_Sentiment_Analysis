import os
import modal
import hopsworks
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
LOCAL=False

if LOCAL == False:
   stub = modal.Stub("twitter_dynamic")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(years=1), secret=modal.Secret.from_name("HOPSWORKS_API_KEY")) # modify "ID2223" to match your modal
   def f():
       g()



def get_dynamic_twi():
    import pandas as pd
    """
    Returns a DataFrame containing 100 tweets
    """
    project = hopsworks.login()
    fs = project.get_feature_store()
    twitter_fg = fs.get_feature_group(name="twi_sentiment_yearly", version=1)
    query = twitter_fg.select_all()
    feature_view = fs.get_or_create_feature_view(name="twi_sentiment_yearly",
                                  version=1,
                                  description="Read from dynamic twitter dataset",
                                  labels=["label"],
                                  query=query)
    i_train, i_test, o_train, o_test = feature_view.train_test_split(0.001)
    df = pd.DataFrame(columns=['text', 'sentiment'])
    df['text'] = i_train
    df['sentiment'] = o_train
    return df


def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login(project="zhihanxu") # modify "zhihanxu" to match your hopsworks project
    fs = project.get_feature_store()

    twi_df = get_dynamic_twi()

    twi_fg = fs.get_feature_group(name="twi_sentiment",version=1)
    twi_fg.insert(twi_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        #stub.deploy("wine_daily")
        modal.runner.deploy_stub(stub)
        f.remote()