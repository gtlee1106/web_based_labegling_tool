from rest_framework import serializers
from .models import DataSet, DataSetItem, DataSetItemLabel


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'


class DataSetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSetItem
        fields = '__all__'


class DataSetItemLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSetItemLabel
        fields = '__all__'
