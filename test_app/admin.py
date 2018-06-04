from django.contrib import admin
from .models import DataSet, DataSetItem, DataSetItemLabel

# Register your models here.
admin.site.register(DataSet)
admin.site.register(DataSetItem)
admin.site.register(DataSetItemLabel)