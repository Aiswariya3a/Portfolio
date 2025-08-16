# mysite/views.py

from django.shortcuts import render
from .models import SiteSetting, Project

def home(request):
    # We fetch the first (and only) SiteSetting object
    settings = SiteSetting.objects.first()
    projects = Project.objects.all()
    context = {
        'settings': settings,
        'projects': projects,
    }
    return render(request, 'mysite/home.html', context)