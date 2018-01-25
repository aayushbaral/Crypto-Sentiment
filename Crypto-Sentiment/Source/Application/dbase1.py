#!/usr/bin/env python3


#Importing needed dependencies
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
from textblob import TextBlob


#Authorization using the app's access tokens

consumer_key  = "ESrMrx02rbo92AII3Cncopxg7"
consumer_secret = "1Pgbd1UixCKFcGhRbiZeFJXaZab6wARmsObKNdVInnE9Qjd6pg"
access_token = "877199751233630208-b0XnzzRWNxliUSw5VOfPZd7bRTeuUG6"
access_token_secret = "OLOFmx8rBRHm7uknkvcN1zttIWnLczBr0aklEUbIVAG2L"


#Mongo Client and creating a database named twitterdb and adding a collection in the database named cryptoinfo
client = MongoClient()
db = client.twitterdb
cryptoinfo = db.cryptoinfo


"""
This is actually an instance if a user defined class which has a method on_data
on_data processes the result and returns true or false
if on_data returns true then it processed the tweet okay and everything is fine
if it returns false then the connection will be shut down. This provides an endless stream of data that
then is dumped into a mongodb database

"""

class StdOutListener(StreamListener):

	def on_data(self, data):
		
		tweets = json.loads(data)
		tweetId = tweets['id_str']
		username = tweets['user']['screen_name']
		text = tweets['text']
		hashtags = tweets['entities']['hashtags']
		date_created = tweets['created_at']
		language = tweets['lang']
		location = tweets['user']['location']

		#Modeling the tweet
		
		tweet = {'tweetId': tweetId, 'username': username, 'text':text, 'hashtags': hashtags, 'datecreated': date_created, 'language': language, 'location': location}
		#Using Textblob method from textblob dependency to get the polarity of the tweet and storing it in the dictionary
		blob = TextBlob(tweet["text"])
		tweet["polarity"] = blob.sentiment.polarity
	
		"""First thought of creating different collections for different crytotypes
		but complication arose while posting the type and getting information from each collection
		"""

		#Getting tweets with language english and not having RT(retweets on it and adding a new attribute cryptotype for different cryptocurrencies.
		if tweet['language'] == "en" and "@RT" not in tweet["text"]:
			if "bitcoin" in tweet["text"]:
				tweet["Cryptotype"] = "bitcoin"

			elif "ethereum" in tweet["text"]:
				tweet["Cryptotype"] = "ethereum"
		
			elif "litecoin" in tweet["text"]:
				tweet["Cryptotype"] = "litecoin"
			else:
				return "No matches found"
		
		else:
			return	

		#Inserting into Mongo Database
		try:
			cryptoinfo.insert(tweet)
		except Exception as e:
			print("Unable to connect to the databasedatabase: {0}".format(e))


#Tweepy's function to 
	def on_error(self, status):
		print(status.text)
		


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filtering the tweets
    stream.filter(track=['bitcoin', 'ethereum', 'litecoin'])
"""When we invoke an API method most of the time returned back to us will be
be a Tweepy model class instance. This will contain the data returned from Twiteer
which we can then use inside our application. 
"""