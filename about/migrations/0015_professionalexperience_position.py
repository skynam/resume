# Generated by Django 2.2.1 on 2019-06-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_auto_20190623_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalexperience',
            name='position',
            field=models.CharField(choices=[('left', 'left'), ('right', 'right')], default='left', max_length=100),
        ),
    ]
