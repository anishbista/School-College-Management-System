from django.db import models
from common.models import CommonInfo
from course_class.models import TimeTable
from accounts.models import Student
# Create your models here.
class AbsentStudent(CommonInfo):
    absentee = models.ManyToManyField(Student)
    sub_class = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_absent = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_absent:
            for student in self.absentee.all():
                # Logic to send email to student's parent
                # subject = 'Absentee Notification'
                # message = f'Your child was absent on {self.date}.'
                # from_email = ''
                # to_email = 
                # send_mail(subject, message, from_email, [to_email])
                pass
        super().save(*args, **kwargs)