# Generated by Django 5.0.4 on 2024-05-03 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 23, 48, 19, 482008), verbose_name='date published'),
        ),
    ]