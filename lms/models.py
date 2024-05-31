from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='courses', null=False, blank=False)
    credit_hour = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    pdf = models.FileField(upload_to='usernotes', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title
