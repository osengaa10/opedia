from django.db import models
from datetime import datetime
from PIL import Image

# Create your models here.
class Researcher(models.Model):
    name = models.CharField(max_length=200)
    researcher_rating = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    lap_the_sun_day = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
