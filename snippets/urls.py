#-*- coding:utf-8 -*-
#django的库
from django.conf.urls import include,url
# 第三方的库
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
# 项目的库
#from .views import snippet_list,snippet_detail
#from .views import SnippetList, SnippetDetail, UserList, UserDetail, SnippetHighlight, api_root
from .views import SnippetViewSet, UserViewSet, api_root


"""
第0种:使用默认的url模式
"""
# urlpatterns = format_suffix_patterns([
#     url(r'^$',api_root),
#     url(r'^snippets/$',SnippetList.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',SnippetDetail.as_view(),name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',SnippetHighlight.as_view(),name='snippet-highlight'),    
#     url(r'^users/$', UserList.as_view(),name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),name='user-detail'),
# ])

"""
第1种:引入了viewset后，我们在url里面使用聚合的router，这里明显的显示出来，方便我们进行跟踪
"""
# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight'
# },renderer_classes=[renderers.StaticHTMLRenderer])
# user_list =UserViewSet.as_view({
#     'get':'list'
# })
# user_detail = UserViewSet.as_view({
#     'get':'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^$',api_root),
#     url(r'^snippets/$',snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',snippet_detail,name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',snippet_highlight,name='snippet-highlight'),    
#     url(r'^users/$', user_list,name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail,name='user-detail'),
# ])
"""
Create a router and register our viewsets with it.
第2种: 我们之前是显示的snippet_list = SnippetViewSet.as_view({'get':'list'}),现在我们使用默认的
router = DefaultRouter()
"""
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)
"""
The API URLs are now determined automatically by the router.
Additionlly,we include the login URLs for the browser API.
url 会自动捆绑到对应的ViewSet
"""
urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^api-auth/$',include('rest_framework.urls', namespace='rest_framework')),
]