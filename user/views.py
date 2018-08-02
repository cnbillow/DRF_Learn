from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from user.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):

    # 自己编写的默认视图集
    # def list(self, request):
    #     # 获取用户集
    #     queryset = User.objects.all()
    #     # 获取用户序列化信息
    #     serializer = UserSerializer(queryset, many=True)
    #     # 返回序列化数据
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     # 获取用户集
    #     queryset = User.objects.all()
    #     # 通过主键查询get_object_or_404
    #     user = get_object_or_404(queryset, pk=pk)
    #     # 获取用户查询集
    #     serializer = UserSerializer(user)
    #     # 返回具体的serializer数据
    #     return Response(serializer.data)

    # 使用提供默认行为集的现有基类
    serializer_class = UserSerializer
    queryset = User.objects.all()

