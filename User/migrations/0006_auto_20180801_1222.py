# Generated by Django 2.0.6 on 2018-08-01 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20180801_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
