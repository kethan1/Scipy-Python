from twitter import Twitter, OAuth
import json

with open("apiKeys.json") as twitter_info:
    twitter_info_dict = json.load(twitter_info)["twitter"]
    twitter = Twitter(
        auth=OAuth(
            twitter_info_dict["consumer_key"],
            twitter_info_dict["consumer_secret"],
            twitter_info_dict["access_token"],
            twitter_info_dict["access_token_secret"],
        )
    )

# Gets user screen_name, and from that gets the user's friends. The screen name
# is the user's twitter handle (https://twitter.com/<screen_name>). Any
# screen_handle can be passed to this, not only the current user's.
# twitter_username = twitter.account.verify_credentials()['screen_name']
twitter_username = input("Enter the twitter whoose friend you want to get, 0 for current user: ")
if twitter_username == "0":
    twitter_username = twitter.account.verify_credentials()['screen_name']
friend_ids = twitter.friends.ids(screen_name=twitter_username)
print(friend_ids)

friends = []
for group_of_friend in range(0, len(friend_ids["ids"]), 100):
    hundred_ids = friend_ids["ids"][group_of_friend: group_of_friend + 100]
    users = [twitter.users.lookup(user_id=user) for user in hundred_ids]
    for user in users:
        friends.append(user[0]["screen_name"])
print(friends)
# print(twitter.users.lookup(user_id=2358139032))
