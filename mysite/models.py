# mysite/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    tech_stack = models.CharField(max_length=500)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    repo_url = models.URLField(max_length=200)
    order = models.PositiveIntegerField(default=0, help_text="Used to order projects. Lower numbers appear first.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    # Add this new method
    def get_tech_stack_as_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('LANGUAGE', 'Programming Language'),
        ('DATABASE', 'Database'),
        ('TOOL', 'Tool/Framework'),
        ('DEVOPS', 'DevOps'),
        ('ML_DL', 'Machine/Deep Learning'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='TOOL')
    level = models.PositiveIntegerField(default=80, help_text="A percentage from 0 to 100.")
    order = models.PositiveIntegerField(default=0, help_text="Used to order skills. Lower numbers appear first.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    site_description = models.TextField(blank=True, help_text="A short description for SEO.")
    site_keywords = models.CharField(max_length=300, blank=True, help_text="Comma-separated keywords for SEO.")
    email = models.EmailField(max_length=200)
    github_url = models.URLField(max_length=200)
    linkedin_url = models.URLField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return "Site Settings"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"