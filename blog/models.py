#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    """
    作者模型
    """
    name = models.CharField(verbose_name =u'姓名', max_length= 30)
    mail = models.EmailField(verbose_name = u'邮箱', max_length=100)

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    """
    文章模型
    """
    STATUS_DRAFT = 'draft'
    STATUS_PUBLIC = 'public'
    STATUS_SET = (
        (STATUS_DRAFT,'草稿'),
        (STATUS_PUBLIC,'公开'),
    )
    title = models.CharField(max_length=100, verbose_name=u'标题')
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    updated_at = models.DateTimeField(default = datetime.now(),verbose_name=u'修改时间')
    status = models.CharField(choices=STATUS_SET, default= STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name = 'entries')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
