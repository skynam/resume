# Generated by Django 2.2.1 on 2019-06-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='select',
            field=models.CharField(choices=[(1, '1'), (2, '2')], default=1, max_length=2),
        ),
    ]
