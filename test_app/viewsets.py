from rest_framework import viewsets
from .models import DataSet, DataSetItem, DataSetItemLabel
from .serializers import DataSetSerializer, DataSetItemSerializer, DataSetItemLabelSerializer


class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


class DataSetItemViewSet(viewsets.ModelViewSet):
    queryset = DataSetItem.objects.all()
    serializer_class = DataSetItemSerializer


class DataSetItemLabelViewSet(viewsets.ModelViewSet):
    queryset = DataSetItemLabel.objects.all()
    serializer_class = DataSetItemLabelSerializer
