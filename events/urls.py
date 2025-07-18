# events/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, basename='event')

urlpatterns = router.urls
