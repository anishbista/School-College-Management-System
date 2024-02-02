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
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="grade",
    )

    def __str__(self):
        return f"level: {self.level} department: {self.department.type}"


class Student(CommonInfo):
    student_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student"
    )
    user_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="student"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=g_choices, max_length=20)
    phone_no = models.CharField(max_length=15)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="student")
    dob = models.DateField()

    def save(self, *args, **kwargs):
        self.student_userName.email = self.email
        self.student_userName.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Teacher(CommonInfo):
    teacher_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher"
    )
    user_role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="teacher"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    dob = models.DateField()

    def save(self, *args, **kwargs):
        self.teacher_userName.email = self.email
        self.teacher_userName.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(CommonInfo):
    course_name = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="course")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="course"
    )

    class Meta:
        unique_together = ("course_name", "grade", "teacher")

    def __str__(self):
        return f"Course: {self.course_name} Grade: {self.grade}"


class Parent(CommonInfo):
    parent_userName = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="parent"
    )
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="parent")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="parent"
    )

    def save(self, *args, **kwargs):
        self.parent_userName.email = self.email
        self.parent_userName.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
