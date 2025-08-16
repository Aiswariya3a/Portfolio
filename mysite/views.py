# mysite/views.py

from collections import defaultdict
from django.shortcuts import render
from .models import SiteSetting, Project, Skill

def home(request):
    settings = SiteSetting.objects.first()
    projects = Project.objects.all()

    # 1. Define the desired order for categories by their display names
    category_order = [
        'Programming Language',
        'Tool/Framework',
        'Database',
        'Machine/Deep Learning',
        'DevOps',
    ]
    
    # 2. Initialize a dictionary with empty lists, respecting the defined order
    grouped_skills = {category: [] for category in category_order}

    # 3. Fetch all skills from the database
    skills_queryset = Skill.objects.all().order_by('order')

    # 4. Populate the dictionary with skills
    for skill in skills_queryset:
        category_name = skill.get_category_display()
        if category_name in grouped_skills:
            grouped_skills[category_name].append(skill)
    
    # 5. (Optional) Filter out any empty categories
    final_grouped_skills = {k: v for k, v in grouped_skills.items() if v}


    context = {
        'settings': settings,
        'projects': projects,
        'grouped_skills': final_grouped_skills,
    }
    return render(request, 'mysite/home.html', context)