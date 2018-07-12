import twitter

#enter your respective keys by making the application.
api = twitter.Api(consumer_key = 'consumer_key',
                  consumer_secret = 'consumer_secret',
                  access_token_key = 'access_token_key',
                  access_token_secret = 'access_token_secret')

user = '@user_name'
statuses = api.GetUserTimeline( screen_name = user, count =30, include_rts=False)

for s in statuses:
    print (s.text)

# to get the people you are following
friends = api.GetFriends(screen_name = user)
for friend in friends:
    print (friend.name)