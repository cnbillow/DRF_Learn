from django.db import models
from datetime import datetime
from model_utils import Choices
from model_utils.fields import StatusField, MonitorField


class Comment(models.Model):
    STATUS = Choices("name", "email", "address")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=40)

    status = StatusField()
    published_at = MonitorField(monitor='status', when=['name', "email", "address"])
