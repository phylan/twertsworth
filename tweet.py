import config
import twitter

api = twitter.Api(
					consumer_key = config.CONSUMER_KEY,
					consumer_secret = config.CONSUMER_SECRET,
					access_token_key = config.ACCESS_TOKEN,
					access_token_secret = config.ACCESS_SECRET
				)
				
def post(tweet):
	if len(tweet) > 140:
		#Shorten the tweet to fit character limit
		tweet = tweet[:140]
	api.PostUpdate(tweet)
	return "Tweeted " + tweet 

	