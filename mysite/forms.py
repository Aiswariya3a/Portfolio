# mysite/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-charcoal text-white p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-neon-teal',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-charcoal text-white p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-neon-teal',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-charcoal text-white p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-neon-teal',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-charcoal text-white p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-neon-teal',
                'placeholder': 'Your Message',
                'rows': 5
            }),
        }