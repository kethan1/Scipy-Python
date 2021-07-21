from twitter import Twitter, OAuth
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

"""
Hypothesis: If a Twitter user has more than 100 friends, than more than 50% of
that user's friends will have more than 100 friends.

Hypothesis, in simpler terms: Popular people tend to be friends with popular people.
"""

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

twitter_username = input("Enter the twitter whoose friend you want to get, 0 for current user: ")
if twitter_username == "0":
    twitter_username = twitter.account.verify_credentials()['screen_name']
friend_ids = twitter.friends.ids(screen_name=twitter_username)
# print(friend_ids)

friends = {
    user_info[0]["screen_name"]: user_info[0]["friends_count"]
    for user in friend_ids["ids"]
    for user_info in [twitter.users.lookup(user_id=user)]
}
print(friends)

if len(friends) < 100:
    print("This person is not popular")
    sys.exit()

number_of_friend_with_more_than_100_friends = 0

for friend, friend_count in friends.items():
    if friend_count > 100:
        number_of_friend_with_more_than_100_friends += 1

if number_of_friend_with_more_than_100_friends < len(friends) / 2:
    print("This person does not have popular friends")
    sys.exit()

bar_indexes = [index for index in range(len(friends))]
plt.bar(bar_indexes, list(friends.values()), align="center")  # Create a bar graph.
plt.xticks(bar_indexes, list(friends.keys()))  # Add the bar names to the graph.
plt.ylabel("Number of Cats and Dogs")
plt.title("Cats and Dogs")
plt.show()
