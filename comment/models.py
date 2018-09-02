from django.db import models

# Create your models here.


class Article(models.Model):
    # 标题
    title = models.CharField(max_length=32)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now_add=True) # auto_now  和 auto_now_add 对于一个字段而言只能写一个，不能同时写
    type = models.SmallIntegerField(
        choices=((1, "原创"), (2, '转载')), default=1) # choice 用于页面上的选择框标签，提供一个二元元组，第一个元素是存在数据库中，
    # 第二个元素表示页面上显示的内容
    school = models.ForeignKey('School', on_delete=models.CASCADE)  # models.CASCADE 表示有关系的记录一并删除
    tag = models.ManyToManyField('Tag')  # 多对多，自动创建关系表


class School(models.Model):
    name = models.CharField(max_length=32)


class Tag(models.Model):
    name = models.CharField(max_length=32)
