import snscrape.modules.twitter as sntwitter
import pandas as pd
from pathlib import Path

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])

filepath = Path('./tweets.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
tweets_df.to_csv(filepath)