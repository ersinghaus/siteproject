from __future__ import unicode_literals

from django.db import models

COURSES = (
    ('Math', 'Math'),
    ('Art', 'Art'),
    ('Science', 'Science'),
    ('History', 'History'),
    ('English', 'English'),
)

class Document(models.Model):
    name = models.CharField(max_length=25, default= 'Enter File Name')
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    courses = models.CharField(max_length=8, choices=COURSES)
