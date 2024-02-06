# Generated by Django 5.0 on 2024-02-06 10:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_rename_parent_name_parent_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student'), ('Teacher', 'Teacher'), ('Parent', 'Parent'), ('Staff', 'Staff')], default='Student', max_length=50),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=20)),
                ('phone_no', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('staff_userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='accounts.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
