# mysite/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Project, ContactMessage, SiteSetting # Import SiteSetting

class PortfolioTests(TestCase):

    def setUp(self):
        """Set up necessary objects for the tests."""
        self.client = Client()
        # Create the SiteSetting object that the contact form view needs
        self.settings = SiteSetting.objects.create(
            site_title="Test Site",
            tagline="A test tagline.",
            email="test-recipient@example.com", # This email will be used in the test
            github_url="http://github.com",
            linkedin_url="http://linkedin.com"
        )

    def test_project_model_creation(self):
        """Test that a Project object can be created and its string representation is correct."""
        project = Project.objects.create(
            title="Test Project",
            slug="test-project",
            short_description="A test.",
            tech_stack="Django, Python",
            repo_url="http://github.com"
        )
        self.assertEqual(str(project), "Test Project")
        self.assertEqual(Project.objects.count(), 1)

    def test_contact_form_submission(self):
        """Test submitting the contact form successfully creates a new ContactMessage."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.'
        }
        
        response = self.client.post(reverse('mysite:home') + '#contact', data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        
        new_message = ContactMessage.objects.first()
        self.assertEqual(new_message.name, 'Test User')