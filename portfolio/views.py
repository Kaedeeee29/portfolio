from django.shortcuts import render
from .models import Skill, Project, SocialLink
from blog.models import Post


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    social_links = SocialLink.objects.all()
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:3]

    skill_categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_categories:
            skill_categories[cat] = []
        skill_categories[cat].append(skill)

    context = {
        'skills': skills,
        'skill_categories': skill_categories,
        'projects': projects,
        'featured_projects': featured_projects,
        'social_links': social_links,
        'recent_posts': recent_posts,
    }
    return render(request, 'portfolio/home.html', context)
