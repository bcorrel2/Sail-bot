""""""""""""""""""""""""""""""""""""""""""
##            sail_bot 1.0    			##

""""""""""""""""""""""""""""""""""""""""""

import time, tweepy, random, string

#---------------Access Key---------------#

consumer_key = 'BsALF0Dtf5AU18lOR8YGCWFN2'
consumer_secret = 'jh7b4xqpZc6iydkuy2augR5uWqsKOY3ihQta1Z0NUHiuXulfAQ'
token_key = '700927951257219072-0vFpGRRTbJAxHOARNXgM3WEpz9vbrI5'
token_secret = 'RXNAG1Q7nESEFBU27G1GOEjk6avXqcFTZL16mihcs9uZe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

#--------------Functions-----------------#

def checkTweet(tweet):
        length = len(tweet)

        if(len(tweet) > 140):
                return False

        else:
                return True

def post(tweet):

	valid = checkTweet(tweet)

	if(valid == False):
		print '-ERROR- Invalid Tweet. Please Modify Tweet Library.'

	else:

		print '-PREPARING-'
		print tweet
		try:
			api.update_status(tweet)

		except tweepy.TweepError:
			print '-ERROR- TweepError'
			return		
	
		print time.asctime(time.localtime(time.time()))
		
		print '-POSTED-'
		print #blank line

def reciFollow():
	
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()

def postCycle(lnum):
	file = open('tweet_file.txt', 'r') #read file
	lines = file.readlines()
	file.close()

	# --- True = Ordered --- False = Random --- #
	mode = True

	length = len(lines)
	
	if(mode == True): 
		lnum = inOrder(lnum, length)

	if(mode == False):
		lnum = randomSeq(lnum, length)

	# ----------------------------------------- #
	print lnum
	print lines[lnum]
	post(lines[lnum])

        if( checkTweet(lines[lnum]) == False ):
                print 'line ' + lnum

        reciFollow()
        time.sleep(60) #60 seconds

	postCycle(it)

def inOrder(old, length):
	new = old+2

	if(new >= length):
		new = 0

	return new

def randomSeq(old, length):
	
	new = old;

	while(new == old):
		new = random.randrange(0,length-1)
	
		if(it % 2 != 0): #If number isn't even
                        it += 1

	return it		

#------------------------------------------#

postCycle(-1)
print '-ERROR- STOP'		
