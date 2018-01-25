#!/usr/bin/env python3

import web
from pymongo import MongoClient


"""This is the web framework for the project
"""

urls = (
'/cryptosentiment/search', 'search', 
'cryptosentiment/details', 'details')

static_render = web.template.render('static/')
template_render =  web.template.render('templates/')


app = web.application(urls, globals())
client = MongoClient()
dbase = client.twitterdb
collection = dbase.cryptoinfo

class search:
	def GET(self):
		return template_render.form()

	def POST(self):
		my_input = web.input().type
		#Limiting the number of tweets we want to display
		limit_input = web.input().limit

		tweet_details = collection.find({"Cryptotype": '{0}'.format(my_input)}).limit(int(limit_input))
		return template_render.bitcoin(tweet_details)
if __name__ == "__main__":
    app.run()