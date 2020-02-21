import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "7ZRs5AtYV997Tmis9JnWMKv1z"
consumer_secret = "FoQOqkwndAeN7wdFKbXtdlmyoGvEKmeHs3bjvyuexWtpD8PKV1"
access_key = "2849778937-xyg9uH795FTYOc0nm6i6ve6xC0w8ulJf8Vs4d1z"
access_secret = "4RFa7O8bSa37tHerJPikLQmA5S4oL0KdfGzFC5AOj6UBY"

tweets_for_csv = []

global tmp
tmp=[]

global tweetRec
tweetRec = 0

# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# Access to user's access key and access secret 
auth.set_access_token(access_key, access_secret) 
  
# Calling api 3
api = tweepy.API(auth) 
  


# Function to extract tweets 
def get_tweets(username,tweetRec): 
          

        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
            tweetRec=tweetRec+1
            # Appending tweets to the empty array tmp 
            tmp.append([tweetRec,username,j])  

    
  
user_handles_array=["southwestair", "brycemanheart"]

for user_handle in user_handles_array:
    # Driver code 
    if __name__ == '__main__': 
  
        # Here goes the twitter handle for the user 
        # whose tweets are to be extracted. 
        get_tweets(user_handle,tweetRec)  
        

print(tmp)




#collecting a list of followers
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for user in tweepy.Cursor(api.friends, screen_name="TechCrunch").items():
    print('friend: ' + user.screen_name)

for user in tweepy.Cursor(api.followers, screen_name="TechCrunch").items():
    print('follower: ' + user.screen_name)
