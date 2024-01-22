from django.db import models
from django.contrib.auth.models import User
from common.models import *
from course_class.models import Grade,Course

class Role(CommonInfo):
    role = models.CharField(choices=r_choices, default="Student", max_length=50)

    def __str__(self):
        return self.role


class Department(CommonInfo):
    type = models.CharField(choices=dp_choices, max_length=100)

    def __str__(self):
        return self.type

class Student(CommonInfo):
    student_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student"
    )
    user_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="student"
    )
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=g_choices, max_length=20)
    phone_no = models.CharField(max_length=15)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="student")
    dob = models.DateField()
    def __str__(self) -> str:
        return self.student_name


class Teacher(CommonInfo):
    teacher_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher"
    )
    user_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="teacher"
    )
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name="teacher"
    )

    def __str__(self):
        return self.teacher_name


class Parent(CommonInfo):
    parent_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="parent"
    )
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="parent")
    parent_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="parent"
    )

    def __str__(self):
        return self.teacher_name
