# Generated by Django 5.0.4 on 2024-05-04 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tutorial_content_alter_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 4, 4, 15, 16, 168244, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
