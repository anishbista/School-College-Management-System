from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task


@shared_task
def send_absence_notification_email(absent_student_email, course_name, teacher_name):
    subject = f"Your Child's Absence Notification - {course_name}"
    message = render_to_string(
        "absence_notification_email.html",
        {
            "course_name": course_name,
            "teacher_name": teacher_name,
        },
    )
    print(f"Message:  {message}")
    print(f"type of message is {type(message)}")
    plain_message = strip_tags(message)
    # The strip_tags function in Django is used to remove HTML tags from a given string, leaving only the plain text content

    print(f"plain message : {plain_message}")
    print("Type of plain message")
    print(type(plain_message))
    send_mail(
        subject,
        plain_message,
        "anishbista9237@gmail.com",
        [absent_student_email],
        html_message=message,
    )


# html_message parameter allows you to send an alternative HTML-formatted version of your email alongside the plain text version. This is useful when you want to provide both HTML and plain text content in your emails to accommodate different email clients and user preferences.
