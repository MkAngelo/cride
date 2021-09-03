"""Cirles urls"""

# Django
from django.urls import path, include   
from rest_framework import urlpatterns

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views

router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='cirlce')

urlpatterns = [
    path('', include(router.urls))
]