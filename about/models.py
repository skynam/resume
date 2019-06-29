from django.db import models
import datetime


class Banner(models.Model):
    banner = models.ImageField(upload_to='about/banner')

    def __str__(self):
        return 'Banner'


class SellingPoint(models.Model):
    selling_point = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.selling_point


class SelfIntroduction(models.Model):
    one_phrase_introduction = models.CharField(max_length=100)
    detailed_introduction = models.TextField()

    def __str__(self):
        return 'Self Introduction'


class WhatIDo(models.Model):
    who_i_am = models.CharField(max_length=100)
    more_about_who_i_am = models.TextField()

    def __str__(self):
        return 'What I do'


class WhatIDoItem(models.Model):
    icon = models.CharField(max_length=100, default='fa-')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return 'What I do listed item'


class Skill(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category


class SkillItem(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        'Skill', default=None, on_delete=models.SET_NULL, null=True)
    how_sufficient_you_are = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProfessionalExperience(models.Model):
    position_set = [
        ('left', 'left'),
        ('right', 'right')
    ]
    year = models.CharField(max_length=4)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    first_day = models.DateField(auto_now=False, default=datetime.date.today)
    last_day = models.DateField(auto_now=False, default=datetime.date.today)
    to_present = models.BooleanField(default=False)
    position = models.CharField(
        max_length=100, choices=position_set, default='left')

    def __str__(self):
        return self.job_title


class Portfolio(models.Model):
    category = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class PortfolioItem(models.Model):
    project_name = models.CharField(max_length=100)
    category = models.ForeignKey(
        'Portfolio', default=None, on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/portfolio')

    def __str__(self):
        return self.project_name


class ContactForm(models.Model):
    headline = models.CharField(max_length=100)
    subline = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return 'Contact Info'


class SocialMedia(models.Model):
    social_media_set = [
        ('fa-twitter', 'Twitter'),
        ('fa-facebook', 'Facebook'),
        ('fa-dribbble', 'Dribbble'),
        ('fa-flickr', 'Flickr'),
        ('fa-github', 'Github')
    ]
    social_media = models.CharField(
        max_length=100, choices=social_media_set, default='fa-twitter')
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.social_media
