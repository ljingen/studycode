#-*- coding:utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'groups', GroupViewSet)
