import requests
import json

news_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
r = requests.get(news_url)
recent = str(r.json()[0])

story_url = 'https://hacker-news.firebaseio.com/v0/item/' + recent + '.json?print=pretty'
x = requests.get(story_url)
details = x.json()

print('Title: ' + details['title'])
print('Author: ' + details['by'])
print('Link: ' + details['url'])
