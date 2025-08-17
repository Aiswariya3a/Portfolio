# mysite/views.py

from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import SiteSetting, Project, Skill
from .forms import ContactForm
import json

def home(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message = contact_form.save() # Save the message to the DB

            # --- Send the email ---
            subject = f"Portfolio: {message.subject}"
            email_message = f"""
            You have a new message from {message.name} ({message.email}).

            Message:
            {message.message}
            """
            send_mail(
                subject,
                email_message,
                'sender@example.com', # This is ignored by the console backend
                [SiteSetting.objects.first().email],
                fail_silently=False,
            )
            # ----------------------

            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('/#contact')
    else:
        contact_form = ContactForm()
    settings = SiteSetting.objects.first()
    projects = Project.objects.all()

    # list of project titles
    projects_data = list(Project.objects.values('title'))
    # list of skill names
    skills_data = list(Skill.objects.values('name'))

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
    contact_form = ContactForm() # Create an instance of the form

    context = {
            'settings': settings,
            'projects': projects,
            'grouped_skills': final_grouped_skills,
            'contact_form': contact_form,
            'projects_json': projects_data,
            'skills_json': skills_data,
        }
    return render(request, 'mysite/home.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    settings = SiteSetting.objects.first() # For base template context
    context = {
        'project': project,
        'settings': settings,
    }
    return render(request, 'mysite/project_detail.html', context)