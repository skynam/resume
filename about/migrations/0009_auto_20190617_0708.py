# Generated by Django 2.2.1 on 2019-06-16 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20190617_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalexperience',
            name='last_day',
            field=models.DateField(default=datetime.date.today),
        ),
    ]