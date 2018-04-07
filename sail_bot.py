import time, tweepy, random, string

#---------------Access Key---------------#

consumer_key = 'SgPN7R5Ili5c5Cvk37bmwfADB'
consumer_secret = 'Ben9qS5eyHd7H10JyrQZJ57pxUI8lXD1ifHXqsPpww7wXsu38o'
token_key = '852938638803566592-6FV88lDJwOVbXveYgnaCUVx4pi4Vmdj'
token_secret = 'e7kS3dsZiOX77Opb4lxqQ3cNz98cx0CS0c5LUzsyDHqPL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

#---------------Functions-----------------#

def checkTweet(tweet):
	# Function for Checking Tweet Validity
	# if < 140 characters, return true, else return false
        length = len(tweet) 

        if(len(tweet) > 140):
                return False

        else:
                return True

def post(tweet):
	# Function for posting to Twitter

        valid = checkTweet(tweet) # Check if tweet is <140 characters

        if(valid == False):
                print '-ERROR- Invalid Tweet. Please Modify Tweet Library.'

        else:

                print '-PREPARING-'
                try:
                        api.update_status(tweet) # post to Twitter

                except tweepy.TweepError: # Twitter returns error
                        print '-ERROR- TweepError'
                        return

                print time.asctime(time.localtime(time.time())) # Time Stamp

                print '-POSTED-'
                print #blank line

# ...
                
def getLine(lastLine, mode, length):
	# Function for determining which Tweet should be posted

		if(mode == False): # Random Mode
	
			rand = random.randrange(0,length)
		
			if(rand%2 != 0):
				rand+=1
			
			if(rand == lastLine):
				rand = getLine(lastLine, mode, length)
			
			return rand
			
		else: # In-Order Mode
		
			if(lastLine+1 < length):
				return lastLine+1

			else:
				return 0    	
    	    
def reciFollow():

        for follower in tweepy.Cursor(api.followers).items():
                follower.follow()	           
    	            
# Execution Block

lnum = -1 # holds the last line number posted

while(1): # infinite loop
	file = open('tweet_file.txt', 'r') #read file
    	lines = file.readlines()
    	file.close()

	length = len(lines) # number of lines in file

	lnum = getLine(lnum, False, length) # True: In-Order False: Random

    	if( checkTweet(lines[lnum]) == False ): # identify problem tweets
    		print '-Error- bad tweet'
    		print # blank line
           
    	else:
        	post(lines[lnum])

        reciFollow()
        
    	time.sleep(60) # sleep 60 seconds


