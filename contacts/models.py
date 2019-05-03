from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=1000)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000, blank=True)
    message = models.TextField(blank=True)
    user_document = models.FileField(upload_to='research_papers/', blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
