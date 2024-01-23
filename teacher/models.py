from django.db import models
from common.models import CommonInfo, attendance_choice
from accounts.models import Teacher, Student, Course
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


class Attendance(CommonInfo):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_class = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=attendance_choice)

    class Meta:
        unique_together = ("teacher", "course_class", "student", "date")

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
