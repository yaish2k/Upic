from datetime import datetime
from django.http import QueryDict
import urllib
from upic_app.serializers.tweet_serializer import TweetsSerializer

tweets_to_insert = [{
                        u'user_id': 2,
                        u'post_id': 3,
                        u'text': "ma kore anasahim ddddd",
                        u'user_image': "https://www.google.com",
                        u'tweet_image': "https://www.google.com",
                        u'time_stamp': datetime.now(),
                        u'place': 1,
                        u'country': "Israel",
                        u'likes': 50
                    },
                    {
                        u'user_id': 2,
                        u'post_id': 3,
                        u'text': "ma kore anasahim ddddd",
                        u'user_image': "https://www.google.com",
                        u'tweet_image': "https://www.google.com",
                        u'time_stamp': datetime.now(),
                        u'place': 1,
                        u'country': "Israel",
                        u'likes': 50
                    },
                    {
                        u'user_id': 2,
                        u'post_id': 3,
                        u'text': "ma kore anasahim ddddd",
                        u'user_image': "https://www.google.com",
                        u'tweet_image': "https://www.google.com",
                        u'time_stamp': datetime.now(),
                        u'place': 1,
                        u'country': "Israel",
                        u'likes': 50
                    }]


def check_dict_type(data):
    if type(data) == dict:
        url_dict = urllib.urlencode(data)
        qdict = QueryDict(url_dict)
        return qdict
    elif type(data) == QueryDict:
        return data


def change_key_value_to_string(list_of_tweets):
    new_list_of_tweets = []
    for tweet in list_of_tweets:
        new_tweet = {str(key): value for key, value in tweet.items()}
        new_list_of_tweets.append(new_tweet)
    print new_list_of_tweets
    return new_list_of_tweets

for tweet in tweets_to_insert:
    print tweet
    serializer = TweetsSerializer(data=tweet)
    if serializer.is_valid():
        print "Blaa"
        serializer.save()
    else:
        print "semmk"
