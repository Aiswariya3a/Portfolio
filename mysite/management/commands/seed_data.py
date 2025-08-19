from django.core.management.base import BaseCommand
from mysite.models import Project, Skill, SiteSetting
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with initial portfolio data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to seed the database...'))
        
        # Logic to clear old data and add new data will go here in the next step.

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))