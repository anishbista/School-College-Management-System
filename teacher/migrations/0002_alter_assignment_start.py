# Generated by Django 5.0.1 on 2024-01-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
