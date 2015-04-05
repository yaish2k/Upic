from django.conf.urls import patterns, include, url
from rest_framework_extensions.routers import ExtendedDefaultRouter
from upic_app.views.place_view_set import PlaceViewSet
from upic_app.views.tweet_view_set import TweetViewSet
from django.contrib import admin

admin.autodiscover()

router = ExtendedDefaultRouter()
(
    router.register(r'places', PlaceViewSet, base_name='places')
        .register(r'tweets', TweetViewSet, base_name='tweets', parents_query_lookups=['place']),
    router.register(r'tweets', TweetViewSet, base_name='tweets')

)

urlpatterns = patterns('',


    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include(router.urls)),
)


