from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=225, null=False, blank=False)
    contact   = models.CharField(max_length=10, null=False, blank=False)
    emil      = models.EmailField(null=True, blank=True)
    message   = models.TextField( null=False, blank=False)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.full_name} - {self.created}"
    
class Notice(models.Model):
    subject = models.CharField(max_length=225, null=False, blank=False)
    desc = models.TextField( null=False, blank=False)
    attachment = models.FileField(upload_to='notices', null=True, blank=True)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.subject} - {self.created}"
    

