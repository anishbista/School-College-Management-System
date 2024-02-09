from django.db import models
from common.models import CommonInfo
from accounts.models import Student,Course
from datetime import date, timedelta
from django.db.models.signals import post_delete
from django.dispatch import receiver


class libraryBook(CommonInfo):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    availability_status = models.BooleanField(default=True)

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


class Driver(CommonInfo):
    driver_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.driver_name


class Bus(CommonInfo):
    bus_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    drive_by = models.ForeignKey(Driver, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "buses"

    def __str__(self) -> str:
        return self.bus_number


class Route(CommonInfo):
    route_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.route_name


class Stop(CommonInfo):
    stop_name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_order = models.IntegerField()

    def __str__(self) -> str:
        return self.stop_name


class Schedule(CommonInfo):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()


class Alert(CommonInfo):
    ALERT_TYPES = (
        ("delay", "Delay"),
        ("schedule_change", "Schedule Change"),
    )

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    alert_message = models.TextField()
    alert_time = models.DateTimeField()

#payment
class Fee(CommonInfo):
    fee_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()
    def __str__(self) -> str:
        return self.fee_name
    
class Payment(CommonInfo):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    def __str__(self) -> str:
        return f"Student:{self.student} fee:{self.fee}"
    class Meta:
        unique_together = ['student', 'fee']

#exam
class Exam(CommonInfo):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField()
    duration = models.CharField(max_length=20)
    status_choices = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    def __str__(self) -> str:
        return f"Course:{self.course} Date:{self.start_date}"
class Result(CommonInfo):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

class Feedback(CommonInfo):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    text = models.TextField()