from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
from textblob import TextBlob
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tweety"
)

#consumer key, consumer secret, access token, access secret.
ckey="dA4N8dSTkW1v1MJV5WmAX6Xo2"
csecret="w9dxAlT4b9W3rIrtw2oLsUtIQKGHLUOb5RlZv8v3DWEeQNb9jx"
atoken="1103910210152747009-W036T1iHJ0VBH4SKnxCC67imC8B2A3"
asecret="TVocGBVP2wsVvWSq51tCzS2oOyZsHUagVxdqYnnEgxDqA"



class listener(StreamListener):

	def on_data(self, data):

		all_data = json.loads(data)
		print(all_data)
		try:
			tweet = all_data["extended_tweet"]["full_text"]
		except:
			tweet = all_data["text"]
		
		wiki = TextBlob(tweet)
		try:
			tweet = str(wiki.translate(from_lang="tl", to='en'))
		except:
			tweet = tweet
		print(wiki.sentiment)
		print(wiki.sentiment.polarity)
		print(wiki.detect_language())
	
		#sentiment_value, confidence = s.sentiment(tweet)
		# if wiki.sentiment>0:
			# print ('Positive')
		# elif wiki.sentiment<0:
			# print ('Negative')
		# else:
			# print ('Neutral')
		mycursor = mydb.cursor()

		sql = 'INSERT INTO `tweets`(`id`, `content`, `sentiment`, `language`, `polarity`,`tweet`) VALUES ("",'+ str(json.dumps(str(all_data))) +',"'+ str(wiki.sentiment.subjectivity) +'","'+str(wiki.detect_language())+'","'+ str(wiki.sentiment.polarity)+'","'+ str(tweet) +'")'
		print(sql)
		mycursor.execute(sql)

		mydb.commit()
		#print(tweet, sentiment_value, confidence)

		#if confidence*100 >= 80:
			#output = open("twitter-out.txt","a")
			#output.write(sentiment_value)
			#output.write('\n')
			#output.close()
	
		print(":)")
		return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener(),tweet_mode='extended')
twitterStream.filter(track=["@enjoyGLOBE , #GlobeAtHome , @LiveSmart , @PLDTHome"])