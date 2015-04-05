from rest_framework import serializers
from upic_app.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place