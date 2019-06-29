from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Banner, SellingPoint, SelfIntroduction, WhatIDo, WhatIDoItem, Skill, SkillItem, ProfessionalExperience, Portfolio, PortfolioItem, ContactForm, SocialMedia
from .forms import ContactForm
from django.contrib import messages
from .mail_function.mail_function import mail_to_me


def form_variable(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            comments = form.cleaned_data.get('comments')
            mail_to_me(name, email, comments)
            messages.success(request, 'Thanks! Will get in touch with you very soon!')
            form = ContactForm()
            return form
    else:
        form = ContactForm()
    return form


def p_year_list(request):
    professional_year_list = []
    for item in ProfessionalExperience.objects.all():
        if item.year not in professional_year_list:
            professional_year_list.append(item.year)
    professional_year_list.sort(reverse=True)
    return professional_year_list


def home(request):
    content = {'banner': Banner.objects.first(), 'selling_point': SellingPoint.objects.all(), 'self_introduction': SelfIntroduction.objects.first(), 'what_i_do': WhatIDo.objects.first(), 'what_i_do_item': WhatIDoItem.objects.all(), 'skill': Skill.objects.all(), 'skill_item': SkillItem.objects.all(
    ), 'professional_experience': ProfessionalExperience.objects.all(), 'professional_experience_year': p_year_list(request), 'portfolio': Portfolio.objects.all(), 'portfolio_item': PortfolioItem.objects.all(), 'social_media': SocialMedia.objects.all(), 'form': form_variable(request)}

    return render(request, 'about/index.html', content)
