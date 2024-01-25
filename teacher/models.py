from datetime import date
from django.db import models
from common.models import CommonInfo, attendance_choice
from accounts.models import Teacher, Student, Course, Grade
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @property
    def is_past_done(self):
        return date.today() > self.end

    def __str__(self):
        return self.name


class Attendance(CommonInfo):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="attendance"
    )
    course_class = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="attendance"
    )
    present_student = models.ManyToManyField(Student, related_name="attendance")
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("teacher", "course_class", "date")

    def __str__(self):
        return f"{self.date} - {self.teacher} -  {self.course_class}"
