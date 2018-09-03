from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path(r'add/', views.add),
    path(r'detail/', views.detail)
]