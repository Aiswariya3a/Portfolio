
from django.urls import path
from . import views

app_name = 'mysite' # app namespace

urlpatterns = [
    path('', views.home, name='home'),
    # Example URL: /project/classroom-monitoring-system/
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
]