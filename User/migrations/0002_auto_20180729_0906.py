# Generated by Django 2.0.6 on 2018-07-29 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 9, 6, 54, 481414, tzinfo=utc)),
        ),
    ]
