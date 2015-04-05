from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from upic_app.models import Place
from upic_app.serializers.place_serializer import PlaceSerializer

class PlaceViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Place.objects.all()
    model = Place
    serializer_class = PlaceSerializer