#-*- coding:utf-8 -*-

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限,只有创建者自己才能进行编辑
    """
    # def has_object_permission(self,request,view,obj):
    #     # # Read permissions are allowed to any request,
    #     # # so we'll always allow GET HEAD or OPTIONs requests.
    #     # if request.method in permissions.SAFE_METHODS:
    #     #     return True
    #     # # write permissions are only allow to the owner of the snippet.
    #     # return obj.owner == request.user
    #     pass
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user