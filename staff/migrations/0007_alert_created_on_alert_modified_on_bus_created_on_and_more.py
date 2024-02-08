# Generated by Django 5.0 on 2024-02-08 11:10

import datetime
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_bus_options_remove_driver_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alert',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='bus',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='driver',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='route',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='stop',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 3, 9)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stop',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]