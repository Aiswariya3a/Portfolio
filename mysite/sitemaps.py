from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        # Returns a list of URL names for the static pages
        return ['mysite:home']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Returns the queryset of all projects
        return Project.objects.all()

    # The location of each project is automatically determined
    # by Django by calling the get_absolute_url().