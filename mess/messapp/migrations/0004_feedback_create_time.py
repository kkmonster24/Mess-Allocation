# Generated by Django 2.0.2 on 2019-05-21 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messapp', '0003_auto_20190521_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]