#!/usr/bin/env python
# encoding: utf-8
"""
---------------------------------------------------------------
IMPORTANT:                                                    |
This program only works in python2 due to the tweepy module   |
---------------------------------------------------------------
"""
import tweepy #https://github.com/tweepy/tweepy
import json
import math
from time import gmtime, strftime, sleep


#Twitter API credentials Get your own API credentials @ apps.twitter.com
consumer_key = "GvgCKnVEX5bRA1ZRjBQPVUCj4"
consumer_secret = "izjOTwcf2OLn8KJWom2zdsCIoHEe1ekEDzenb82whGpeNz4EHn"
access_key = "318449791-OUeKzhbSdbQzcy29bK3nkjAqqfEHxHFY9teugrYY"
access_secret = "qOnRIANIw0mXj51CORPs4ePqlwkfRh80vudbTGqyLe9Jt"


def writeTweetsToJson(screen_name):
    """This function downloads up to 3200 tweets from a specified twitter profile"""

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #Indicates when the sequence to gather the tweets starts.
    print "Tweets from " + screen_name + " are now being downloaded."

    #Empty list where the tweets will be gathered.
    alltweets = []

    #Downloads 200 tweets at the time (200 tweets is the maxium tweepy can handle at the time)
    new_tweets = api.user_timeline(screen_name = screen_name, count = 200)

    #Saves the tweets to the empty list
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #As long as there are tweets, keep gathering tweets.
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevena
        new_tweets = api.user_timeline(screen_name = screen_name, count=200, max_id = oldest)

        #Adds the tweets.
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet.
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded...." % (len(alltweets))
        print strftime("%a, %d %b %Y %H:%M:%S", gmtime())

    #Dump all the tweets to a JSON file.
    file = open(screen_name + "tweets.json", "wb")
    print "Creating a JSON File...."
    for status in alltweets:
        json.dump(status._json,file, sort_keys = True, indent = 4)

    #Closes the JSON file when the tweets are dumped.
    print "Tweets from " + screen_name + " are downloaded and saved."
    print "_" * 40
    file.close()


def get_word_count(account):
    jsonData = open(account+"tweets.json", "r+")
    lines = jsonData.readlines()
    tweets = []

    for line in lines:
        for word in line: #Should be if line.startswith("text") but python parses json files weird.
            tweets.append(word)
    print math.floor((len(tweets)) / 140),  "words has", account, "tweeted!"
    jsonData.close()

    wordCount = """ "wordCount" """ ":"

    if account == "@bjorklundjan":
        jsonData = open("fighter6.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@annieloof":
        jsonData = open("fighter1.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@SwedishPM":
        jsonData = open("fighter2.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@jsjostedt":
        jsonData = open("fighter4.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@cbildt":
        jsonData = open("fighter3.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@jimmieakesson":
        jsonData = open("fighter5.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    elif account == "@BuschEbba":
        jsonData = open("fighter7.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()
    else:
        jsonData = open("fighter8.json", "w")
        jsonData.write("{" + "\n" + wordCount + str(len(tweets) / 140) + "\n" + "}")
        jsonData.close()

if __name__ == "__main__":
    #Write what twitter profiles tweets you want to download (CASE SENSITIVE), if you enter a name of a profile you already have the old file will be overwritten.
    while True:
        writeTweetsToJson("@jimmieakesson")
        writeTweetsToJson("@SwedishPM")
        writeTweetsToJson("@IsabellaLovin")
        writeTweetsToJson("@annieloof")
        writeTweetsToJson("@cbildt")
        writeTweetsToJson("@jsjostedt")
        writeTweetsToJson("@bjorklundjan")
        writeTweetsToJson("@BuschEbba")
        get_word_count("@annieloof")
        get_word_count("@bjorklundjan")
        get_word_count("@BuschEbba")
        get_word_count("@cbildt")
        get_word_count("@IsabellaLovin")
        get_word_count("@jimmieakesson")
        get_word_count("@jsjostedt")
        get_word_count("@SwedishPM")
        print("_" * 40)
        print("Done!")
        print("_" * 40)
        sleep(500)
