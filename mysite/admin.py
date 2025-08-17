from django.contrib import admin
from .models import Project, Skill, SiteSetting, ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('created_at',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'tech_stack')
    search_fields = ('title', 'tech_stack')
    # Automatically fills the 'slug' field based on the 'title'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Skill)
admin.site.register(SiteSetting)