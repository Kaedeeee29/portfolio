from django.contrib import admin
from django import forms
from .models import Skill, Project, SocialLink


class SocialLinkForm(forms.ModelForm):
    url = forms.CharField(max_length=200)  # plain CharField, no URL validation
    
    class Meta:
        model = SocialLink
        fields = '__all__'


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    form = SocialLinkForm
    list_display = ['name', 'url', 'order']
    list_editable = ['order']


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