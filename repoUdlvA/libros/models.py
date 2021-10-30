from django.db import models

# Create your models here.

FACULTY_CHOICES = ((0, 'N/A'),(1, 'Ciencia y Tecnología'), (2, 'Bellas Artes'),
(3, 'Educación'), (4, 'Ciencias Sociales'), (5, 'Ingeniería'))

class librosmodel(models.Model):
    title = models.CharField(max_length=100)
    faculty = models.IntegerField(choices=FACULTY_CHOICES, null=0)
    abstract = models.TextField(blank=True)
    editorial = models.CharField(max_length=50, blank=True)
    author_or_authors = models.CharField(max_length=250,blank=True)
    key_words = models.CharField(max_length=100, blank=True)
    URL = models.URLField(max_length=200, blank=True)
    file = models.FileField(upload_to='files/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

