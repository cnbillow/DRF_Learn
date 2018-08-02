from django.shortcuts import render
from rest_framework import serializers
from datetime import datetime
# Create your views here.


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email="xql@163.com", content="serializer")


