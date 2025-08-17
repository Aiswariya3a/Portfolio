# mysite/admin.py

from django.contrib import admin
from .models import Project, Skill, SiteSetting, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(SiteSetting)
admin.site.register(ContactMessage)