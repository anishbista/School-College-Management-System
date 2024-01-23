from django.db import models
from common.models import CommonInfo
from accounts.models import Student,Course,Grade
from django.core.validators import FileExtensionValidator
# Create your models here.
class Assignment(CommonInfo):
    name=models.CharField(max_length=50)
    description=models.TextField()
    start=models.DateTimeField(auto_now_add=True)
    end=models.DateTimeField()
    image=models.ImageField(null=True,blank=True)
    hw_file = models.FileField(upload_to='media/', validators=[FileExtensionValidator(['pdf', 'docx'])],null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Submit(CommonInfo):
    work=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    sb_file = models.FileField(upload_to='media/', validators=[FileExtensionValidator(['pdf', 'docx'])],null=True,blank=True)
class Feedback(CommonInfo):
    fk=models.TextField()
    fk_work=models.ForeignKey(Submit,on_delete=models.CASCADE)