# Generated by Django 5.0 on 2024-02-07 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_driver_route_alter_borrowing_due_date_bus_alert_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'buses'},
        ),
        migrations.RemoveField(
            model_name='driver',
            name='contact_person',
        ),
    ]
