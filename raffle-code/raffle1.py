import tweepy
import random
import pprint
import csv
import pandas as pd
from sets import Set
####input your credentials here
TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
unique_screen_names = Set()
screen_to_name_map = {}
for tweet in tweepy.Cursor(api.search,q="#sugcon #searchstax #solr #sitecore",count=100,
                           lang="en",
                           since="2019-05-15", show_user=True).items():
    print (tweet.user.screen_name, tweet.user.name,tweet.created_at, tweet.text)
    unique_screen_names.add(tweet.user.screen_name)
    screen_to_name_map[tweet.user.screen_name] = tweet.user.name
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.user.name, tweet.text.encode('utf-8')])

#pprint.pprint(unique_screen_names)
pprint.pprint(len(unique_screen_names))
print 'PARTICIPANTS'
for participant in unique_screen_names: 
    print "%s (%s)" % (screen_to_name_map[participant], participant)

winner = random.choice(list(unique_screen_names))
print '---------'
print "Winner: %s (%s)" % (screen_to_name_map[winner], winner)
