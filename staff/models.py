from django.db import models
from common.models import CommonInfo
from accounts.models import Student
from datetime import date,timedelta

class libraryBook(CommonInfo):
    name=models.CharField(max_length=100,unique=True,blank=False,null=False)
    author=models.CharField(max_length=100,blank=False,null=False)
    availability_status=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
class Borrowing(CommonInfo):
    book = models.ForeignKey(libraryBook, on_delete=models.CASCADE)
    borrowed_person = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrowing_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=date.today() + timedelta(days=30))