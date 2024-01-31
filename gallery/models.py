from django.db import models
from common.models import CommonInfo
# Create your models here.
class Gallery(CommonInfo):
    image=models.ImageField(upload_to="gallery/",blank=False,null=False)
    description=models.TextField()
    name=models.CharField(max_length=100)
    date=models.DateField()