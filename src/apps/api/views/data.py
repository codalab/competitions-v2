from rest_framework.viewsets import ModelViewSet

from api import serializers
from datasets.models import Data, DataGroup


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer


class DataGroupViewSet(ModelViewSet):
    queryset = DataGroup.objects.all()
    serializer_class = serializers.DataGroupSerializer
