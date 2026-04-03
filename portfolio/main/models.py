from django.db import models


class SiteProfile(models.Model):
    name          = models.CharField(max_length=100)
    tagline       = models.CharField(max_length=200)
    short_bio     = models.TextField()
    about         = models.TextField()
    career_goals  = models.TextField()
    email         = models.EmailField()
    github        = models.URLField(blank=True)
    linkedin      = models.URLField(blank=True)
    twitter       = models.URLField(blank=True)

    class Meta:
        verbose_name        = "Site Profile"
        verbose_name_plural = "Site Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORIES = [
        ('backend',  'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('tools',    'Tools'),
        ('hardware', 'Hardware'),
    ]
    name        = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80)
    category    = models.CharField(max_length=20, choices=CATEGORIES, default='backend')
    order       = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    emoji       = models.CharField(max_length=10, default='🚀')
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tech        = models.CharField(max_length=500, help_text="Comma separated: Java, MySQL")
    github_url  = models.URLField(blank=True)
    live_url    = models.URLField(blank=True)
    featured    = models.BooleanField(default=True)
    order       = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech.split(',') if t.strip()]


class Education(models.Model):
    school      = models.CharField(max_length=200)
    degree      = models.CharField(max_length=200)
    year        = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order       = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.school}"


class ContactMessage(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    subject    = models.CharField(max_length=200)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"