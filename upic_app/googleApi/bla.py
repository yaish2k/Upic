# from google import search
# result = search("pubs in ibiza",stop=20)
# for url in result:
#     print url
# import urllib2
# url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyAjfO3M8f9LSukw54OBUv4W3eGnTVKa1VE"
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()
# print "******************************************************"
# url2 = "https://www.google.co.il/?gws_rd=ssl#q=pubs+in+ibiza"
# request = urllib2.Request(url2)
# response = urllib2.urlopen(request)
# print response.read()
from upic_app.models import Place, Tweets
print Place.objects.all()
print Tweets.objects.all()
