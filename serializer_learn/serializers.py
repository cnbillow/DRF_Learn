from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=500)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)
        # 对象保存到数据库
        # return Comment.objects.all(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.content = validated_data.get("content", instance.content)
        instance.created = validated_data.get('created', instance.created)
        # 对象保存到数据库
        # instance.save()
        return instance