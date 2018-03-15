import urllib2
import json
from upic_app.models import Place
from upic_app.serializers.place_serializer import PlaceSerializer

class PlaceHandler(object):
    def __init__(self):
        self.all_places = Place.objects.all()

    def get_places_by_query_string(self,query_string):
        """
        get list of places from googlemaps api by queryString
        return : place list
        """
        list_query_string = query_string.split(' ')
        new_query_string = "+".join(list_query_string)
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s' % (new_query_string, google_key)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = json.load(response)
        return result['results']


    def filter_places_field(self,list_of_places):
        """
        create new list of dicts filtered by only Adress,X,Y and name
        :param list_of_places:
        :return: new place list
        """
        new_list_of_places = []
        for place in list_of_places:
            current_place_dict = {}
            current_place_dict["place_id"] = place["place_id"]
            current_place_dict["adress"] = place["formatted_address"]
            current_place_dict["name"] = place["name"]
            current_place_dict["lat"] = place["geometry"]["location"]["lat"]
            current_place_dict["long"] = place["geometry"]["location"]["lng"]
            new_list_of_places.append(current_place_dict)

        return new_list_of_places

    def change_key_values_to_unicode(self,list_of_places):
        """
        param: list_of_places
        this function change the key of each place in te list to unicode which it must for the PlaceSerializer to know this is model object
        return: new list
        """
        new_list_of_places = []
        for place in list_of_places:
            new_place = {unicode(key) : value for key,value in place.items()}
            new_list_of_places.append(new_place)

        return new_list_of_places

    def check_if_place_is_exists(self,place_id):
        """
        check if the place is already exists in db by place id
        :param place_id
        :return boolean
        """
        for place in self.all_places:
            if place.place_id == place_id:
                return False

        return True

    def insert_place_to_db(self,list_of_places):
        """
        this function pass over the list and insert to db each place
        """
        for place in list_of_places:
            if self.check_if_place_is_exists(place['place_id']):
                print "true"
                print place
                place_serializer = PlaceSerializer(data=place)
                if place_serializer.is_valid():
                    print "success"
                    place_serializer.save()
            else:
                print "false"



handler = PlaceHandler()
new_list = handler.get_places_by_query_string("pubs in new york")
new_list2 = handler.filter_places_field(new_list)
new_list3 = handler.change_key_values_to_unicode(new_list2)
handler.insert_place_to_db(new_list3)
