# Sail_bot Testing 3: Automation

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

def getRandomTweet(last_tweet, length):
    # Function for determining which tweet should be posted - randomly
    # @param last_tweet: Integer holding line no. of the previous tweet
    # @param length: Integer holding length of tweets.txt
    # @return line no. of selected tweet
    
    line_no = random.randint(0,length-1)
    
    if(line_no % 2 != 0): # Avoid empty lines
        line_no += 1
    
    while(line_no == last_tweet): # Get new line
        line_no = getRandomTweet(last_tweet, length-1)
    
    return line_no

def getInlineTweet (last_tweet, length):
    # Function for determining which Tweet should be posted - in order
    # @param last_tweet: Integer holding line no. of the previous tweet
    # @param length: Integer holding length of tweets.txt
    # @return line no. of next tweet
    
    if(last_tweet + 1 < length): # return next tweet
        return last_tweet + 1
    
    else: # all tweets have been posted
        return -2

# -------Execution Block ------- #

lastline = -1 # holds the last line number posted

while(1): # infinite loop
    tweet_file = open('tweets.txt', 'r') # read file
    lines = tweet_file.readlines()
    tweet_file.close()
    
    length = len(lines) # number of lines in file
    
    lastline = getRandomTweet(lastline, length)
    
    if( checkTweet(lines[lastline]) == False ): # identify problem tweets
        print '-Error- bad tweet'
        print # blank line
    
    else:
        postTweet(lines[lastline])
    
    time.sleep(60) # sleeps specified time (in seconds)



