# Generated by Django 5.0 on 2024-01-10 14:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('level', models.CharField(choices=[('11', '11'), ('12', '12')], max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='accounts.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('course_name', models.CharField(max_length=100)),
                ('descriptions', models.TextField(max_length=500)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='course_class.grade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField()),
                ('tclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_class.grade')),
                ('tcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_class.course')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
