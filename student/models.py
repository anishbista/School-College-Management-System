from django.db import models
from common.models import CommonInfo
from teacher.models import *


class Submit(CommonInfo):
    work = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    sb_file = models.FileField(
        upload_to="media/",
        validators=[FileExtensionValidator(["pdf", "docx"])],
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Submission"
