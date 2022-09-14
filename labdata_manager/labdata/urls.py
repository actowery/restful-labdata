from rest_framework import routers
from .api import LabdataViewSet


router = routers.DefaultRouter()
router.register('api/labdata', LabdataViewSet, 'labdata')

urlpatterns = router.urls