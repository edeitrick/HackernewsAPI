import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Test1: Validate if an integer was returned
# Test2: Validate if the news is the most recent
def getRecentNewsIDs():
    news_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    r = requests.get(news_url)
    recent = r.json()[:10]
    return recent

# Test1: Validate if a dictionary was returned
# Test2: Validate if the get request passed through
def getRecentNewsStory(recent_IDs):
  news_stories = {'Title': [], 'Author': [], 'Time posted': []}
  for ID in recent_IDs:
    story_url = 'https://hacker-news.firebaseio.com/v0/item/' + str(ID) + '.json?print=pretty'
    x = requests.get(story_url)
    story = x.json()
#     print(story)
    news_stories['Title'].append(story['title'])
    news_stories['Author'].append(story['by'])
    news_stories['Time posted'].append(story['time'])
  return news_stories

# Test1: Validate if the dataframe was created
def convertToDataframe(recent_story):
  detframe = pd.DataFrame.from_dict(recent_story)
  return detframe


recent_IDs = getRecentNewsIDs()
news_stories = getRecentNewsStory(recent_IDs)
story_dataframe = convertToDataframe(news_stories)
engine = create_engine('mysql://root:codio@localhost/'+'hackernews'+'?charset=utf8', encoding='utf-8')
story_dataframe.to_sql('Most_recent_news_stories', con=engine, if_exists='replace', index=False)


