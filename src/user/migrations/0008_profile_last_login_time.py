# Generated by Django 4.0.6 on 2022-11-18 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]