#-*- coding:utf-8 -*-
# 引入系统库
from datetime import datetime
# 引入django库
from django.db import models
# 引入第三方库
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# 引入自己的库
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS] )
STYLE_CHOICES = sorted((item,item) for item in get_all_styles())
# Create your models here.


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank = True, default='', verbose_name =u'标题')
    code = models.TextField(verbose_name=u'代码')
    created = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    linenos = models.BooleanField(default= False, verbose_name=u'行')
    language = models.CharField(choices = LANGUAGE_CHOICES, default= 'python',max_length=100, verbose_name=u'语言')
    style = models.CharField(choices = STYLE_CHOICES, default='friendly', max_length=100, verbose_name ='类型')
    # 新增加的字段
    owner = models.ForeignKey('auth.User', related_name='snippets', verbose_name=u'创建者',default=1)
    highlighted = models.TextField(default='',verbose_name=u'高亮')
    
    class Meta:
        verbose_name = '代码片段'
        verbose_name_plural = verbose_name
        ordering = ('created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        使用pygments来创建高亮的HTML代码
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title':self.title} or {}
        formatter = HtmlFormatter(style = self.style, linenos=linenos,full=True,**options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet,self).save(*args,**kwargs)
