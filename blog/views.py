# -*- coding:utf-8 -*-
from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import User,Entry
from .serializer import UserSerializer, EntrySerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    User表的视图集合，含有GET PUT PUSH POST DELETE 
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    Entry文章表的视图集合，含有GET  PUT   PUSH  POST  DELETE
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
    #filter_fields = ('author', 'status')

