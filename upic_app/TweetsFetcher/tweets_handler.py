class TweetsHandler(object):
    def __init__(self):
        pass

    def get_tweets_by_coordinate(self,place):
        """
        call dvir alg and return list of tweets by place coordiantes
        """
        pass

    def change_key_values_to_unicode(self,list_of_tweets):
        """
        param: is list of tweets that we get from the alg by place search and this function change the key for each tweet in the list to unicode which it
        must for the TweetsSerializer to know this is model object
        return: new list
        """
        pass

    def insert_tweets_to_db_by_place_id(self,list_of_tweets,place_id):
        """
        this function pass over the list and insert to db each tweet with the place id that passed as param
        """
