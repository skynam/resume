from django.shortcuts import render
from django.http import HttpResponse
from .models import Banner, SellingPoint, SelfIntroduction, WhatIDo, WhatIDoItem, Skill, SkillItem, ProfessionalExperience, Portfolio, PortfolioItem, ContactForm, SocialMedia


def home(request):

    professional_year_list = []
    for item in ProfessionalExperience.objects.all():
        if item.year not in professional_year_list:
            professional_year_list.append(item.year)
    professional_year_list.sort(reverse=True)

    for item in Portfolio.objects.all():
        item.category_str = '.' + ''.join(item.category.lower())

    content = {'banner': Banner.objects.first(), 'selling_point': SellingPoint.objects.all(), 'self_introduction': SelfIntroduction.objects.first(), 'what_i_do': WhatIDo.objects.first(), 'what_i_do_item': WhatIDoItem.objects.all(), 'skill': Skill.objects.all(), 'skill_item': SkillItem.objects.all(
    ), 'professional_experience': ProfessionalExperience.objects.all(), 'professional_experience_year': professional_year_list, 'portfolio': Portfolio.objects.all(), 'portfolio_item': PortfolioItem.objects.all(), 'contact_form': ContactForm.objects.first(), 'social_media': SocialMedia.objects.all()}

    return render(request, 'about/index.html', content)
