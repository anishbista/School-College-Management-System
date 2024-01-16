from django.db import models
from common.models import CommonInfo,l_choices
# Create your models here.
class Grade(CommonInfo):
    level = models.CharField(choices=l_choices, max_length=10)
    department = models.ForeignKey(
        'accounts.Department',
        on_delete=models.CASCADE,
        related_name="grade",
    )
    def __str__(self):
        return f"level: {self.level} department: {self.department.type}"

class Course(CommonInfo):
    course_name = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="course")
    def __str__(self):
        return f"Course: {self.course_name}"

class TimeTable(CommonInfo):
    tname=models.ForeignKey('accounts.Teacher',on_delete=models.CASCADE)
    tclass=models.ForeignKey(Grade,on_delete=models.CASCADE)
    tcourse=models.ForeignKey(Course,on_delete=models.CASCADE)
    start=models.TimeField()
    end=models.TimeField()
    date=models.DateField()