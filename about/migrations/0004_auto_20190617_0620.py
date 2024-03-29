# Generated by Django 2.2.1 on 2019-06-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_contactform_portfolio_portfolioitem_professionalexperience_skill_skillitem_socialmedia_whatido_whati'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalexperience',
            name='to_present',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='year',
            field=models.CharField(choices=[(2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020')], default=2010, max_length=2),
        ),
    ]
