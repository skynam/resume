# Generated by Django 2.2.1 on 2019-06-23 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_professionalexperience_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillitem',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.Skill'),
        ),
    ]