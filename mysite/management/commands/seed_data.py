from django.core.management.base import BaseCommand
from django.utils.text import slugify
from mysite.models import Project, Skill, SiteSetting

class Command(BaseCommand):
    help = 'Seeds the database with the latest portfolio data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to seed the database with updated data...'))
        
        # --- Clean slate ---
        self.stdout.write("Deleting existing data...")
        Project.objects.all().delete()
        Skill.objects.all().delete()
        SiteSetting.objects.all().delete()

        # --- Create Site Settings (Updated) ---
        self.stdout.write("Creating site settings...")
        SiteSetting.objects.create(
            site_title="Aiswariya S",
            tagline="AI Enthusiast | Web Innovator",
            site_description="Personal portfolio of Aiswariya S, a Computer Science graduate and AI developer who specialises in machine learning projects and intelligent web solutions.",
            site_keywords="Aiswariya3a, AI developer, Python, Django, Machine Learning, Portfolio, Computer Science",
            email="aiswariya3a@gmail.com",
            github_url="https://github.com/Aiswariya3a",
            linkedin_url="https://www.linkedin.com/in/Aiswariya3a/"
        )

        # --- Create Skills (Updated) ---
        self.stdout.write("Creating skills...")
        skills_data = [
            {'name': 'Python', 'category': 'LANGUAGE', 'level': 95},
            {'name': 'C', 'category': 'LANGUAGE', 'level': 75},
            {'name': 'Java', 'category': 'LANGUAGE', 'level': 60},
            {'name': 'Flask', 'category': 'TOOL', 'level': 90},
            {'name': 'Django', 'category': 'TOOL', 'level': 85},
            {'name': 'FastAPI', 'category': 'TOOL', 'level': 70},
            {'name': 'MySQL', 'category': 'DATABASE', 'level': 80},
            {'name': 'MongoDB', 'category': 'DATABASE', 'level': 60},
            {'name': 'CNN', 'category': 'ML_DL', 'level': 85},
            {'name': 'OpenCV', 'category': 'ML_DL', 'level': 80},
            {'name': 'Git', 'category': 'DEVOPS', 'level': 90},
            {'name': 'Docker', 'category': 'DEVOPS', 'level': 80},
        ]
        for i, skill in enumerate(skills_data):
            Skill.objects.create(name=skill['name'], category=skill['category'], level=skill['level'], order=i)
        
        # --- Create Projects (Updated) ---
        self.stdout.write("Creating projects...")
        projects_data = [
            {
                'title': "Classroom Monitoring System",
                'short_description': "An AI-powered system to analyze classroom engagement using deep learning for facial expression recognition and pose tracking.",
                'long_description': "Led the development of a comprehensive system to analyze and quantify classroom engagement. Leveraging deep learning algorithms for facial expression recognition and pose tracking, it provides teachers with actionable, real-time insights. The backend was built with Flask, demonstrating a strong grasp of Python-based web frameworks and computer vision libraries.",
                'tech_stack': "Python, Deep Learning, Computer Vision, Flask",
                'repo_url': "https://github.com/Aiswariya3a/CMS_NEC",
            },
            {
                'title': "AI Chart Captioning System",
                'short_description': "A web app that analyzes charts using computer vision and generates contextual captions with Google's Gemini API.",
                'long_description': "Spearheaded a project to create a web application for automated chart analysis. The system uses a VGG19 computer vision model for chart-type detection and integrates Google's Gemini API for generating insightful, contextually relevant captions. The application was built using Streamlit and FastAPI, showcasing skills in modern Python web tools and large language model integration.",
                'tech_stack': "Python, Streamlit, FastAPI, VGG19",
                'repo_url': "https://github.com/Aiswariya3a/AI-Chart-Captioning-System",
            },
            {
                'title': "Fake Account Detector - Instagram",
                'short_description': "A machine learning model deployed with Django to identify fake user accounts based on their profiles.",
                'long_description': "Developed a fake account detection system for Instagram using machine learning. The model, built with TensorFlow and scikit-learn, analyzes profile data to identify patterns indicative of fake accounts. The system was deployed as a web service using the Django framework, demonstrating end-to-end machine learning project capabilities.",
                'tech_stack': "Python, Django, TensorFlow, scikit-learn",
                'repo_url': "https://github.com/Aiswariya3a/Fake-Account-Detector-instagram-",
            },
        ]
        
        for i, project_data in enumerate(projects_data):
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'slug': slugify(project_data['title']),
                    'short_description': project_data['short_description'],
                    'long_description': project_data['long_description'],
                    'tech_stack': project_data['tech_stack'],
                    'repo_url': project_data['repo_url'],
                    'order': i
                }
            )
            if created:
                self.stdout.write(f"  - Created project: {project.title}")

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))