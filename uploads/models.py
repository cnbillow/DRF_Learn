from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='my_book', related_query_name='book')


class User(models.Model):
    name = models.CharField(max_length=32)
    img = models.ImageField(upload_to='images/')
    introduce = models.FileField(upload_to='introduce/')

    def __str__(self):
        return self.name


