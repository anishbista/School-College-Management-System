# Generated by Django 5.0 on 2024-02-09 04:09

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_role_role_staff'),
        ('staff', '0011_alter_payment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 3, 10)),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('text', models.TextField()),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.result')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
