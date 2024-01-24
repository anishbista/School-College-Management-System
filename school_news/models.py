from django.db import models
from common.models import CommonInfo
# Create your models here.
class Holiday(CommonInfo):
    name=models.CharField(max_length=50)
    type=models.TextField(max_length=200)
    start=models.DateField()
    end=models.DateField()
class Event(CommonInfo):
    name=models.CharField(max_length=50)
    descriptions=models.TextField()
    image=models.ImageField()
    start=models.DateTimeField()
class Announcement(CommonInfo):
    name=models.CharField(max_length=50)
    image=models.ImageField()
    descriptions=models.TextField()