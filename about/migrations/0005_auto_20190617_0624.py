# Generated by Django 2.2.1 on 2019-06-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20190617_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalexperience',
            name='to_present',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
