"""DRF_Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from user.views import UserViewSet
#
# # 一般不这样搞
# # # 将视图集绑定到两个单独的视图
# # user_list = UserViewSet.as_view({"get": "list"})
# # user_detail = UserViewSet.as_view({"get": "retrieve"})
#
# from rest_framework.routers import DefaultRouter
#
# # 建议这样使用
# router = DefaultRouter()
# router.register(r'users', UserViewSet, base_name="user")
# urlpatterns = router.urls
from django.contrib import admin
from django.urls import path, include

from comment import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'article_list/', views.article_list),
    path(r'uploads/', include('uploads.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)