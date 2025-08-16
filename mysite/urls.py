# mysite/urls.py (new file)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]