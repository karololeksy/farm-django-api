from django.urls import include, path
from rest_framework import routers
from .views import SheepViewSet

router = routers.DefaultRouter()
router.register(r'sheep', SheepViewSet, basename="sheep")

urlpatterns = [
    path('', include(router.urls)),
]