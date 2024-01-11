# Generated by Django 5.0 on 2024-01-11 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='sb_file',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx'])]),
        ),
    ]
