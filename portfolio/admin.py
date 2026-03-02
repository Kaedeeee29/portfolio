from django.contrib import admin
from django import forms
from .models import Skill, Project, SocialLink


class SocialLinkAdminForm(forms.ModelForm):
    url = forms.CharField(max_length=200, help_text="e.g. https://github.com/user or mailto:you@email.com")

    class Meta:
        model = SocialLink
        fields = '__all__'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_editable = ['featured', 'order']
    list_filter = ['featured']
    search_fields = ['title', 'description']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    form = SocialLinkAdminForm
    list_display = ['name', 'url', 'order']
    list_editable = ['order']