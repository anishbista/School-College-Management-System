from django.db import models
from common.models import CommonInfo
from teacher.models import *

from django.core.exceptions import ValidationError


class Submit(CommonInfo):
    work = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="submission"
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    sb_file = models.FileField(
        upload_to="media/",
        validators=[FileExtensionValidator(["pdf", "docx"])],
        null=True,
        blank=True,
    )
    feedback = models.TextField(blank=True)
    checked = models.BooleanField(default=False)

    def clean(self):
        if not self.image and not self.sb_file:
            raise ValidationError("You must upload either an image or a file.")

    class Meta:
        verbose_name = "Submission"
