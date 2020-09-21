from django.urls import path
from apps.testapp.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('viewset-test/modifier', viewset_test.ModifierViewSet, basename='modifier')
urlpatterns = router.urls
