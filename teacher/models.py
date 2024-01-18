from django.db import models
from common.models import CommonInfo
from accounts.models import Teacher, Student
from django.core.validators import FileExtensionValidator


# Create your models here.
class Assignment(CommonInfo):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    image = models.ImageField(null=True, blank=True)
    hw_file = models.FileField(
        upload_to="assignment/",
        validators=[FileExtensionValidator(["pdf", "docx"])],
        null=True,
        blank=True,
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
