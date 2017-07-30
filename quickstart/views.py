#-*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
