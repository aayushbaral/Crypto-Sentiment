# final-project-aayush-baral-db
final-project-aayush-baral-db created by GitHub Classroom

# Twitter Sentiment Analysis on cryptocurrencies
Extracting recent tweets on cryptocurrencies and displaying the text, location and sentiment of the tweets.

# Description
In this project, I am using Twitter’s Streaming API to download recent tweets using three word filters; bitcoin, ethereum and litecoin. The extracted tweets are inserted into a mongodb database and a web.py framework allows user to retrieve tweets on bitcoin, ethereum and litecoin. The user can limit the tweets they want to display depending upon the size of the database. The user can also look at the sentiment of the tweet which is evaluated using textblob library in python. This project uses mongodb as a DBMS, tweepy to extract tweets, web.py to build a web framework and textblob to do sentiment analysis.

# Getting Started Guide
Step 1:
Download Python 3.5 or above
To install the required libraries
pip3 install -r ..\Source\config\requirement.txt

Step2:
Inside Source\Application
In command line:
Create a mongodb database named “twitterdb” with a collection named “currencies”. 
Run dbase1.py to download all the tweets. As I am using the streaming API it is going to keep downloading tweets. Terminate the process after 30 seconds, this will download around 300 tweets for testing. 
Now we have tweets stored in a mongodb database

To run the web framework:
In command line: Run interface1.py. Go to Google Chrome and type localhost:8080/cryptosentiment/search and you are good to go.



