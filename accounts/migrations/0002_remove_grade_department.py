# Generated by Django 5.0 on 2024-01-09 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='department',
        ),
    ]
