# mysite/views.py

from django.shortcuts import render
from .models import SiteSetting

def home(request):
    # We fetch the first (and only) SiteSetting object
    settings = SiteSetting.objects.first()
    context = {
        'settings': settings,
    }
    return render(request, 'mysite/home.html', context)