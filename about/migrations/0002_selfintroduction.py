# Generated by Django 2.2.1 on 2019-06-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfIntroduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_phrase_introduction', models.CharField(max_length=100)),
                ('detailed_introduction', models.TextField()),
            ],
        ),
    ]
