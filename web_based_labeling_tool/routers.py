from rest_framework import routers
from test_app.viewsets import DataSetViewSet, DataSetItemViewSet, DataSetItemLabelViewSet

router = routers.DefaultRouter()

router.register(r'dataset', DataSetViewSet)
router.register(r'datasetitem', DataSetItemViewSet)
router.register(r'datasetitemlabel', DataSetItemLabelViewSet)
