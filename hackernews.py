import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Test1: Validate if an integer was returned
# Test2: Validate if the news is the most recent
def getRecentNewsID():
    news_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    r = requests.get(news_url)
    recent = r.json()[0]
    return recent

# Test1: Validate if a dictionary was returned
# Test2: Validate if the get request passed through
def getRecentNewsStory(recent_ID):  
    story_url = 'https://hacker-news.firebaseio.com/v0/item/' + str(recent_ID) + '.json?print=pretty'
    x = requests.get(story_url)
    details = x.json()
    return details

# Test1: Validate if the dataframe was created
def convertToDataframe(recent_story):
  detframe = pd.DataFrame.from_dict(recent_story, orient='index')
  return detframe


recent_ID = getRecentNewsID()
recent_story = getRecentNewsStory(recent_ID)
print(recent_story)
story_dataframe = convertToDataframe(recent_story)
engine = create_engine('mysql://root:codio@localhost/hackernews')
story_dataframe.to_sql('Most_recent_news_story', con=engine, if_exists='replace', index=False)


