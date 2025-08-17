from django.contrib import admin
from .models import Project, Skill, SiteSetting, ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(SiteSetting)