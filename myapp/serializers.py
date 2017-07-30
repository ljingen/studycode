#MyTutorial/myapp/serializers.py
#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals, absolute_import
import json

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import MyModel
