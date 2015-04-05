from rest_framework import serializers
from upic_app.models import Tweets

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets