from django.db import models
from django.contrib.auth.models import User
from common.models import *


class Role(CommonInfo):
    role = models.CharField(choices=r_choices, default="Student", max_length=50)

    def __str__(self):
        return self.role


class Department(CommonInfo):
    type = models.CharField(choices=dp_choices, max_length=100)

    def __str__(self):
        return self.type


class Grade(CommonInfo):
    level = models.CharField(choices=l_choices, max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"level: {self.level} department: {self.department.type}"


class Course(CommonInfo):
    course_name = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f"Course: {self.course_name}"


class Student(CommonInfo):
    student_userName = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=g_choices, max_length=20)
    phone_no = models.CharField(max_length=15)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    dob = models.DateField()


class Teacher(CommonInfo):
    teacher_userName = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class Parent(CommonInfo):
    parent_userName = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name
