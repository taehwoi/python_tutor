# import means we are going to use this library(or module.)
import tweepy

consumer_key = 'FILLMEIN'
consumer_secret =  'FILLMEIN'
access_token = 'FILLMEIN'
access_token_secret = 'FILLMEIN'

class MyStreamListener(tweepy.StreamListener):
    # number of on_status reports we will get
    cnt = 100
    # we save our records here
    collections = []

    """override the on_status method"""
    def on_status(self, status):
        #this is called everytime a new twit shows up.
        name = status.user.name
        text = status.text
        self.collections.append((name, text))
        print(name, " said: ", text)

        # decrement count
        cnt -= 1
        if cnt == 0:
            return False

    """override the on_error method"""
    def on_error(self, status_code):
        #420 means that we have reached our query limit
        #wait for 15 minutes?
        if status_code == 420:
            #returning False in on_error disconnects the stream
            print("we have reached our limit")
            return False

        # returning non-False reconnects the stream, with backoff.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

a = input("Word you want to track: ")
#note: track can be a list of words, not just a word
myStream.filter(track=[a])
print(myStreamListener.collections)
