import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

raw_tweets = pd.read_json(r'farmers-protest-tweets-2021-03-5.json', lines=True)
raw_tweets = raw_tweets[raw_tweets['lang']=='en']
print("Shape: ", raw_tweets.shape)
raw_tweets.head(5)

def retweeted(raw_tweets):
    ordenados = raw_tweets.sort_values(by="retweetCount", ascending=False)
    ordenados.head(10)

def emitidos(raw_tweets):
    raw_tweets['cantidad tweets'] = raw_tweets.groupby('id').value_counts()
    ordenados = raw_tweets.sort_values(by="cantidad tweets", ascending=False)
    ordenados.head(10)