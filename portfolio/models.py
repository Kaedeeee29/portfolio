from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('frontend', 'Frontend Technologies'),
        ('backend', 'Backend & Systems'),
        ('tools', 'Tools & Others'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Percentage 0-100")
    icon = models.CharField(max_length=100, blank=True, help_text="Devicon class e.g. devicon-python-plain")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    technologies = models.CharField(max_length=500, help_text="Comma-separated: Python, Django, React")
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome class e.g. fab fa-github")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
