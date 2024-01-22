# Generated by Django 5.0.1 on 2024-01-18 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_assignment_end_alter_assignment_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='hw_file',
            field=models.FileField(blank=True, null=True, upload_to='assignment/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx'])]),
        ),
    ]