from django.contrib import admin
from .models import *


# Register your models here.


"""

class StudentInLine(admin.TabularInline):
    model = Student
    extra = 1


class TeacherInLine(admin.TabularInline):
    model = Teacher
    extra = 1


class ParentInLine(admin.TabularInline):
    model = Parent
    extra = 1


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    inlines = (
        StudentInLine,
        TeacherInLine,
        ParentInLine,
    )
    list_display = [
        "role",
        "get_grade",
    ]

    def get_grade(self, obj):
        return obj.student.first().grade

    get_grade.short_description = "Grade"


admin.site.register(Department)

"""


class GradeInLine(admin.TabularInline):
    model = Grade
    extra = 1


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["role"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        GradeInLine,
    ]
    list_display = ["type"]


# admin.site.register(Department)


# @admin.register(Grade)
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ["level"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "course_name",
        "teacher",
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_userName",
        "student_name",
        "grade",
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "teacher_userName",
        "teacher_name",
        "course",
    ]


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = [
        "parent_userName",
        "parent_name",
        "student",
    ]
