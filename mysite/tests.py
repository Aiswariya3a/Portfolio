from django.test import TestCase
from .models import Project
from .forms import ContactForm

class ProjectModelTest(TestCase):
    """
    Tests for the Project model.
    """
    def test_project_str_representation(self):
        """Test that the string representation of a project is its title."""
        project = Project.objects.create(
            title="My Test Project",
            slug="my-test-project",
            short_description="A test.",
            long_description="A longer test.",
            tech_stack="Django, Python",
            repo_url="http://github.com/test"
        )
        self.assertEqual(str(project), "My Test Project")


class ContactFormTest(TestCase):
    """
    Tests for the ContactForm.
    """
    def test_form_is_valid_with_correct_data(self):
        """Test that the form is valid when all fields are filled correctly."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Hello There',
            'message': 'This is a test message from a valid form.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_missing_name(self):
        """Test that the form is invalid if the required 'name' field is empty."""
        form_data = {
            'name': '',
            'email': 'test@example.com',
            'subject': 'Hello There',
            'message': 'This message should not validate.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_invalid_with_bad_email(self):
        """Test that the form is invalid if the email format is incorrect."""
        form_data = {
            'name': 'Test User',
            'email': 'not-a-valid-email',
            'subject': 'Hello There',
            'message': 'This message should also not validate.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
