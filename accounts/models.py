from django.db import models
from django.contrib.auth.models import User
from common.models import *

class SchoolUser(CommonInfo):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(choices=r_choices,default="Student",max_length=50)
    def __str__(self):
        return self.user.username
class Department(CommonInfo):
    type=models.CharField(choices=dp_choices,max_length=100)
    def __str__(self):
        return self.type
class Grade(CommonInfo):
    level=models.CharField(choices=l_choices,max_length=10)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.level
class Student(CommonInfo):
    student_user=models.ForeignKey(SchoolUser,on_delete=models.CASCADE)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    gender=models.CharField(choices=g_choices,max_length=20)
    phone_no=models.CharField(max_length=15)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)
    dob=models.DateField()