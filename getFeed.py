from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import numpy as np
import time
from datetime import datetime
from threading import Timer
import json
import matplotlib.pyplot as plt

ckey = 'AJuNp5j13MBnciO2KM2DHY93X'
csecret = 'B7pdSc7FqrhCpVdsKCpgjPsKNd7NrgYKpzVAj8skd667Rbmrjt'
atoken = '2959074856-yjJBf97qlz01iijxZDh78BQBueim4PxWC82XRkv'
asecret = 'qoRzHxo7LmipRkesc6X9DiSuC1xT9gJYMvYGYOqoRynrZ'
auth = OAuthHandler(ckey, csecret)

auth.set_access_token(atoken, asecret)

secs = int(raw_input("Please enter number of seconds the stream to run"))
tweetWord = raw_input("Please enter the # tag or a word to fetch information")
test = []
class listener(StreamListener):
	def on_data(self, data):
		test.append(data)
		return True
	def on_error(self, status):
		print status

def exitfunc():
    print "Exit Time", datetime.now()
    print test.__len__()
    plotGraph()
    os._exit(0)
Timer(secs, exitfunc).start()

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[tweetWord], async = True, encoding="utf-8")

def plotGraph():
	loc = []
	for i in range(0, test.__len__()):
		a = json.loads(test[i]).get("user").get("time_zone")
		loc.append(a.__str__())

	unique = set(loc)
	uniqueList = list(unique)

	locDict = {}

	for i in range(0, uniqueList.__len__()):
		locDict[uniqueList[i]] = loc.count(uniqueList[i])
	try:
		X = np.arange(len(locDict))
		fig, ax = plt.subplots()
		plt.bar(X, locDict.values(), align='center', width=0.5)
		plt.xticks(X, locDict.keys())
		ymax = max(locDict.values()) + 1
		plt.ylim(0, ymax)
		fig.autofmt_xdate()
		fig.canvas.set_window_title('No. of tweets from different Time Zones in '+secs.__str__()+" seconds")
		plt.show()
	except:
		print "No tweets have been recorded for "+tweetWord+" within "+secs.__str__()+" seconds"


