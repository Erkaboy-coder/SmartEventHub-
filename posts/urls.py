# events/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet   # PostViewSet ni ham import qilamiz

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')  # shu yerda qo‘shasan

urlpatterns = router.urls
