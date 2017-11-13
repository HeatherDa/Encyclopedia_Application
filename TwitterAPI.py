import tweepy

def getKeys():
    file = open("twitterKeys.txt","r")
    consumerKey = file.readline().rstrip("\n")
    consumerSecret = file.readline().rstrip("\n")
    accessToken = file.readline().rstrip("\n")
    accessTokenSecret = file.readline().rstrip("\n")
    file.close()
    return consumerKey,consumerSecret,accessToken,accessTokenSecret

class TwitterAPI():
    #initiaing information for the twitter api
    def __init__(self):
        self.users = []

        self.consumerKey,self.consumerSecret,self.accessToken,self.accessTokenSecret = getKeys()

        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken,self.accessTokenSecret)
        self.api = tweepy.API(auth)
    #call this method with a query for results
    #the method returns a list within a list
    #Example list[USER][USER_INFO]
    # USERS = 10
    #information stored in USER INFO:
    # 0= name , 1 = screen_name, 2 = creation date, 3 = tweet
    def getTweets(self,query):
        tweets = self.api.search(q=query,count = 10,show_user = True,include_entities=True)

        for tweet in tweets:
            user = []
            user.append(tweet.user.name)
            user.append(tweet.user.screen_name)
            user.append(tweet.created_at)
            user.append(tweet.text)
            self.users.append(user)

        return self.users


#EXAMPLE CODE
#api = TwitterAPI()
#users = api.getTweets("potatoes")
#prints the second user's tweet
#print(users[1][3])
#prints the creation date of the first user's tweet
#print(users[0][2])
