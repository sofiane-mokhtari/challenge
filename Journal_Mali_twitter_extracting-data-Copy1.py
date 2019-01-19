import tweepy, sys, re
import numpy as np
from textblob import TextBlob
import pandas as pd

CONSUMER_KEY    = 'PvzeEvDvTXhyRtPxFXFCSOx4U'
CONSUMER_SECRET = 'nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt'
ACCESS_TOKEN  = '1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU'
ACCESS_SECRET = 'AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z'

def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()
tweets = extractor.user_timeline(screen_name="Yguichaoua ", tweet_mode = 'extended', count=300)
armyv = []
for t in tweets:
    for word in ["francais", "français", "francaises", "française", "francaise", "France"]:
        if word in t.full_text.lower():
            armyv.append(t)
            print(t.full_text)
print(len(armyv))
print(len(tweets))

data = pd.DataFrame(data=[tweet.full_text for tweet in armyv], columns=['Tweets'])

data['len']  = np.array([len(tweet.full_text) for tweet in armyv])
data['ID']   = np.array([tweet.id for tweet in armyv])
data['Date'] = np.array([tweet.created_at for tweet in armyv])
data['Source'] = np.array([tweet.source for tweet in armyv])
data['Likes']  = np.array([tweet.favorite_count for tweet in armyv])
data['RTs']    = np.array([tweet.retweet_count for tweet in armyv])

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))
