from django.contrib import admin
from .models import Banner, SellingPoint, SelfIntroduction, WhatIDo, WhatIDoItem, Skill, SkillItem, ProfessionalExperience, Portfolio, PortfolioItem, ContactForm, SocialMedia


class BannerAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        super().has_add_permission(request)
        if len(SelfIntroduction.objects.all()) >= 1:
            return False
        else:
            return True


class SellingPointAdmin(admin.ModelAdmin):
    list_display = ('selling_point', 'description')

    def selling_point(self, obj):
        return obj.selling_point

    def description(self, obj):
        return obj.description


class SelfIntroductionAdmin(admin.ModelAdmin):
    list_display = ('one_phrase_introduction', 'detailed_introduction')

    def has_add_permission(self, request):
        super().has_add_permission(request)
        if len(SelfIntroduction.objects.all()) >= 1:
            return False
        else:
            return True

    def one_phrase_introduction(self, obj):
        return obj.one_phrase_introduction

    def detailed_introduction(self, obj):
        return obj.detailed_introduction


class WhatIDoAdmin(admin.ModelAdmin):
    list_display = ('what_i_do', 'more_about_what_i_do')

    def has_add_permission(self, request):
        super().has_add_permission(request)
        if len(SelfIntroduction.objects.all()) >= 1:
            return False
        else:
            return True

    def what_i_do(self, obj):
        return obj.who_i_am

    def more_about_what_i_do(set, obj):
        return obj.more_about_who_i_am


class WhatIDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')

    def icon(self, obj):
        return obj.icon

    def title(self, obj):
        return obj.title

    def description(self, obj):
        return obj.description


class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'description')

    def category(self, obj):
        return obj.category

    def description(self, obj):
        return obj.description


class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'how_sufficient_you_are')

    def title(self, obj):
        return obj.title

    def category(self, obj):
        return obj.category

    def how_sufficient_you_are(self, obj):
        return obj.how_sufficient_you_are


class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'year', 'to_present', 'position')

    def job_title(self, obj):
        return obj.job_title

    def year(self, obj):
        return obj.year

    def to_present(self, obj):
        return obj.to_present

    def position(self, obj):
        return obj.position


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('category','tag')

    def category(self, obj):
        return obj.category

    def tag(self, obj):
        return obj.tag

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'category')

    def project_name(self, obj):
        return obj.project_name

    def category(self, obj):
        return obj.category


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subline', 'address', 'phone')

    def has_add_permission(self, request):
        super().has_add_permission(request)
        if len(SelfIntroduction.objects.all()) >= 1:
            return False
        else:
            return True

    def headline(self, obj):
        return obj.headline

    def subline(self, obj):
        return obj.subline

    def address(self, obj):
        return obj.address

    def phone(self, obj):
        return obj.phone


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('social_media', 'link')

    def social_media(self, obj):
        return obj.social_media

    def link(self, obj):
        return obj.link

admin.site.register(Banner, BannerAdmin)
admin.site.register(SellingPoint, SellingPointAdmin)
admin.site.register(SelfIntroduction, SelfIntroductionAdmin)
admin.site.register(WhatIDo, WhatIDoAdmin)
admin.site.register(WhatIDoItem, WhatIDoItemAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillItem, SkillItemAdmin)
admin.site.register(ProfessionalExperience, ProfessionalExperienceAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
