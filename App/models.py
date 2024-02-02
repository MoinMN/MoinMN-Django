from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.CharField('Email', max_length=100)
    subject = models.CharField('Subject', max_length=1000)
    message = models.TextField()

    def __str__(self):
        return self.name