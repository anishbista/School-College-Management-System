from django.db import models
from common.models import CommonInfo
from accounts.models import Student
from datetime import date,timedelta
from django.db.models.signals import post_delete
from django.dispatch import receiver

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
    def save(self, *args, **kwargs):
        self.book.availability_status = False
        self.book.save()
        super().save(*args, **kwargs) 
@receiver(post_delete, sender=Borrowing)
def update_availability_status(sender, instance, **kwargs):
    instance.book.availability_status = True
    instance.book.save()

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.driver_name


class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    drive_by = models.ForeignKey(Driver, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "buses"
    def __str__(self) -> str:
        return self.bus_number

class Route(models.Model):
    route_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.route_name

class Stop(models.Model):
    stop_name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_order = models.IntegerField()
    def __str__(self) -> str:
        return self.stop_name

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

class Alert(models.Model):
    ALERT_TYPES = (
        ('delay', 'Delay'),
        ('schedule_change', 'Schedule Change'),
    )

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    alert_message = models.TextField()
    alert_time = models.DateTimeField()