import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd

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

followers_array=[]

# Function to extract tweets 
def get_tweets(username): 
          

        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        for tweet in tweets:
            tmp.append({"User":username, "Tweets":tweet.text, "Time":tweet.created_at})



#collecting a list of followers
for user in tweepy.Cursor(api.followers, screen_name="brycemanheart").items():
    followers_array.append(user.screen_name)
    print(user.screen_name)
    

for user_handle in followers_array:
    # Driver code 
    if __name__ == '__main__': 
        try:
            # Here goes the twitter handle for the user 
            # whose tweets are to be extracted. 
            get_tweets(user_handle)  
        except:
            continue

twitterData=pd.DataFrame(tmp)
twitterData.to_csv('C:/Users/Laptop/Documents/tweetset.csv')
print(tmp)




