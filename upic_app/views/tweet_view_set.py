from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from upic_app.models import Tweets
from upic_app.serializers.tweet_serializer import TweetsSerializer

class TweetViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Tweets.objects.all()
    model = Tweets
    serializer_class = TweetsSerializer