# Sail_bot Testing 2: Posting

import time, tweepy, random, string

#--------------Access Keys----------------#

consumer_key = 'Enter-Your-Keys-Here'
consumer_secret = 'Enter-Your-Keys-Here'
token_key = 'Enter-Your-Keys-Here'
token_secret = 'Enter-Your-Keys-Here'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
account = tweepy.API(auth)

#---------------Functions-----------------#

def checkTweet(tweet):
    # Function for checking tweet validity
    # @param tweet: String containing tweet
    # @return True if valid, False if not
    
    if(len(tweet) > 280):
        return False
    return True

def postTweet(tweet):
    # Function for posting to Twitter
    # @param tweet: String containing tweet
    
    time_stamp = ""
    
    valid = checkTweet(tweet) # Check if tweet is <280 characters
    
    if(valid == False):
        print '-ERROR- Invalid Tweet'

    else:
        
        print '-PREPARING-'
        
        try:
            account.update_status(tweet) # Post to Twitter
            time_stamp = time.asctime(time.localtime(time.time()))
        
        except tweepy.TweepError: # Twitter returns error
            print '-ERROR- TweepError'
            return
    
        print time_stamp
        print '-POSTED-'
        print #blank line

# -------Execution Block ------- #

tweet = raw_input("Enter Your Tweet: ")
postTweet(tweet)
