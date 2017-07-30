#-*- coding:utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Snippet
from .models import LANGUAGE_CHOICES,STYLE_CHOICES

"""
第1种:继承自Serializer这个基础序列器
显式的定义创建一个Serializer类，在这个Serrializer类里面，对数据库的每个字段都进行覆盖 
实现create,update,delete等方法
"""
# class SnippetSerializer(serializers.Serializer):
#     """
#     方法一:继承自Serializer这个基础序列器
#     显式的定义创建一个Serializer类，在这个Serrializer类里面，对数据库的每个字段都进行覆盖 
#     实现create,update,delete等方法
#     数据序列化用数据的方式:
#     serializer = SnippetSerializer(snippet)
#     serializer.data # 返回一个ReturnDict类型的list
#     content = JSONRender().render(serializer.data) # 把序列化后的数据变为Json数据
#     content # 此时的content就是一个json数据

#     反过来的操作：
#     from django.utils.six import BytesIO
#     stream = BytesIO(content)
#     data = JSONParser().parse(content) 
#     serializer = SnippetSerializer(data=data)  #返回的数据是一个ReturnDict类型list
#     serializer.is_valide() 验证是否是正确数据
#     serializer.validated_data 取到数据
#     serializer.save() 把数据保存成一个Snippet对象 
#     """
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required = False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required = False)
#     language = serializers.ChoiceField(choices= LANGUAGE_CHOICES,default='python')
#     style = serializers.ChoiceField(choices = STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         如果数据合法，就创建并返回一个snippet实例
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         @instance :
#         @validated_data:
#         如果数据合法，就更新并返回一个存在的snippet实例
#         """
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('title',instance.title)
#         instance.linenos = validated_data.get('title',instance.title)
#         instance.language = validated_data.get('title',instance.title)
#         instance.style = validated_data.get('title',instance.title)
#         instance.save()
#         return instance
"""
第2种: 继承自ModelSerializer,和Form.ModelForm类似，我们在Serializer里面也有ModelSerializer数据序列化用数据
的方式,对User这个外键进行序列化.
"""
# class UserSerializer(serializers.ModelSerializer):
    
#     snippets = serializers.PrimaryKeyRelatedField(many = True,queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id','username','snippets')


# class SnippetSerializer(serializers.ModelSerializer):
#     """
#     数据序列化用数据的方式:
#     serializer = SnippetSerializer(snippet)
#     serializer.data # 返回一个ReturnDict类型的list
#     content = JSONRender().render(serializer.data) # 把序列化后的数据变为Json数据
#     content # 此时的content就是一个json数据

#     反过来的操作：
#     from django.utils.six import BytesIO
#     stream = BytesIO(content)
#     data = JSONParser().parse(content)
#     serializer = SnippetSerializer(data=data)  #返回的数据是一个ReturnDict类型list
#     serializer.is_valide() 验证是否是正确数据
#     serializer.validated_data 取到数据
#     serializer.save() 把数据保存成一个Snippet对象 
#     """
#     #owner = UserSerializer()
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ('id','title','code','linenos','language','style','owner','highlighted')

"""
第3种:使用HyperlinkedModelSerializer替代ModelSerializer,在Hyperlineed里面有如下优势：
 (1)HyperlinkedModelSerializer默认不包含主键
 (2)HyperlinkedModelSerializer自动包含URL字段HyperlinkedidentityField
 (3)使用HyperlinkedRelatedField代替PrimaryKeyRelatedField
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name ='snip:snippet-detail',read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='snip:user-detail')    

    class Meta:
        model = User
        fields = ('url','username','snippets')
        


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source ='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snip:snippet-highlight', format='html')
    """
    当时遇到一个问题，因为采用xx:xxx的 url命名方式，导致url一直无法找到
    """
    #url = serializers.SerializerMethodField('get_snippet_url') # 
    url = serializers.HyperlinkedIdentityField(view_name='snip:snippet-detail')    

    class Meta:
        model = Snippet
        fields = ('url','title','code','linenos','language','style','owner','highlight')

    # def get_snippet_url(self, obj):
    #     # generate the url for the key
    #     url = reverse('snip:snippet-detail')