# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route
from rest_framework import permissions
from rest_framework.reverse import reverse

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    print('我是snip:user-list的回调函数值:'+reverse('snip:user-list'))
    return Response({
        'users':reverse('snip:user-list', request=request, format=format),
        'snippets':reverse('snip:snippet-list', request=request,format=format),
})

# # 第一种方法:我们直接使用django的代码，实现基础的rest_framework，验证mehtod方法，然后根据结果进行区分.
# # 使用 JSONResponse进行返回， JSONRenderer().render(serializer.data) JSONParser().parse(request)
# # class JSONResponse(HttpResponse):
# #     """
# #     用于返回JSON数据
# #     就像之前演示的例子
# #     serializer = SnippetSerailizer(sinppet)  # 获取序列化器
# #     serializer.data  #返回的是一个RunDict标准化Python数据
# #     """
# #     def __init__(self, data, **kwargs):
# #         content = JSONRenderer().render(data)  # data 是一个已经序列化的数据  例如data = serializer.data, serializer = SnippetSerializer(snippet)
# #         kwargs['content_type'] = 'application/json'
# #         super(JSONResponse, self).__init__(content, **kwargs)
    

# @csrf_exempt
# def snippet_list(request):
#     """
#     展示所有的snippets，或者创建新的snippet。
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         #return JSONResponse(serializer.data)
#         return Respo
#     elif request.method=='POST':
#         data = JSONParser().parse(request)  # 根据json格式从请求中获取到data
#         serializer = SnippetSerializer(data = data) # 根据json数据获取一个序列号器
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
        

# @csrf_exempt  #装饰器，是的
# def snippet_detail(request, pk):
#     """
#     修改或者删除一个snippet.
#     对于GET方法
#     snippet = Snippet.objects.get(pk = pk)
#     serializer = SnippetSerializer(snippet)
#     对于PUT方法
#     data = JSONParser().paerser(request)
#     serializer = SnippetSerializer(data = data)
#     对于DELETE方法
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status =404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         content = JSONRenderer().render(serializer.data)
#         return JSONResponse(serializer.data)

#     elif request.method =='PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status =400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(stauts = 204)

"""
第2中方法:使用函数视图，引入 rest_framework.response.Response和rest_framework.request.Request,
"""

# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     """
#     展示或者创建snippets
#     """
#     if request.method == 'GET':
#         snipets = Snippet.objects.all()
#         serializer = SnippetSerializer(snipets,many=True)
#         return Response(serializer.data) # rest_framework.response.Response会返回带有一些标题样式的html
#         #return HttpResponse(JSONRenderer().render(serializer.data)) #仅仅返回干净的Json字符串
#     if request.method == 'POST':
#         serializer =SnippetSerializer(data = request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     修改或者删除一个snippet，根据pk先取得到底是那个snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer = SnippetSerializer(snippet, data = request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method =='DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"""
第3种方法:使用类视图来编写API的View视图,使用纯净的APIView,在list类里面，实现对get方法和post方法的实现
get方法:收到get，将snippet都查出来，然后序列化后，返回给客户端json数据
post方法:从post里面接收到数据，生成序列器，验证数据是否正确，正确就保存，然后返回客户端json数据并加上201标识符

SnippetDetail:
get方法:根据pk，取出snippet，并序列化后，返回给前段json数据
"""

# class SnippetList(APIView):
#     """
#     List all snippets,or create a new snippet.
#     """
#     def get(self,request, format= None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)


#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)       


# class SnippetDetail(APIView):
#     """
#     retrieve, update or delete a snippet instance.
#     """
#     def get_object(self,pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#             return snippet
#         except Snippet.DoesNotExist:
#             return HTTP404

#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"""
第4种，因为在APIView里面使用了很多的重复代码，类如save,delete,get等，本章引入mixins，在mixin里面列举了不少
的save,delete,get,put等操作
"""
from rest_framework import mixins
from rest_framework import generics
# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()  # 定义一个queryset
#     serializer_class = SnippetSerializer  # 分配一个序列器的类

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer  # 没括号，是调用这个本身

#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def delete(self, request,*args, **kwargs):
#         return self.destroy(request,*args,**kwargs)
"""
第5种: 我们更进一步,使用通用类视图让代码更简洁,这样我们直接将 mixins.ListModelMixin.....等等都给聚合起来
"""
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     # 增加权限限制
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     # 增加权限限制
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
"""
这段代码是用来显示Html高亮显示。
"""
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
"""
第6种: 我们更进一步,我们使用ViewSet来直接聚合View，ViewSet仅在被调用的时候才会和对应的方法进行绑定，我们将使用
UserViewSet来代替 UserList和UserDetail视图，
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这个视图集合将自动提供 'list'和 'detail'的行为，替代原来的 UserList(generice.ListAPIView) 
    UserDetail(generics.RetrieveAPIView),但需要在URL也针对Viewsets进行对应的整合,ReadOnlyModelViewSet提供
    只读的权限。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
