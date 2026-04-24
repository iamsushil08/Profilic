from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)  # e.g. "Full Stack Developer"
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tool', 'Tools & Others'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)  # percentage 0-100

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    tech_stack = models.CharField(max_length=200)  # e.g. "Django, React, PostgreSQL"
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    date = models.DateField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)  # blank if ongoing
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"