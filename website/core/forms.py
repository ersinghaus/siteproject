from django import forms

from Website.core.models import Document

COURSES = (
    ('Math', 'Math'),
    ('Art', 'Art'),
    ('Science', 'Science'),
    ('History', 'History'),
    ('English', 'English'),
)

class DocumentForm(forms.ModelForm):
    courses = forms.ChoiceField(choices=COURSES, required=True)    
    class Meta:
        model = Document
        fields = ('name', 'document', 'description', 'courses')

