import tweepy #installs library to work with the twitter api 
import time

consumer_key = '0nopFcWl6Zlp3ErdSq8alhAqS'
consumer_secret = 'yl3vUkx5Gg4wwRxoMUu1UeC6qgkwBXUJ4U5uCo0qHIZXbbSVWM'
access_token = '1706878351716261888-7hTMoyjAcW9QXslrqUIpus98S8FYdl'
access_token_secret = 'a2IJIsW0bIj7xOd6oDlSaxbHMFxADCPame5WLH2RW92ZZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) #to authenticate for whichever key needed 

user = api.me() 
# print(user)     # it gives all the details, like name, scree_name, location, and various other info. gives all infor about me- the user
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "bitcoin"
numberOfTweets = 2

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("Sleeping now....")
            time.sleep(50)    # sleeps for 10 secs for it doesnt crash the server 
            #uses cursor to follow back all follwers - too much to do it manualy, prints all followers  


search_string = "python"
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string)
    try: 
        tweet.favorite()
        print('I liked that tweet')
         except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break #only for specific tweets with the particular string 

# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == 'Usernamehere':
#         print(follower.name)
#         follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break #so it wont keep looping 

