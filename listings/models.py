from django.db import models
from datetime import datetime
from researchers.models import Researcher
from PIL import Image

# Create your models here.
class Listing(models.Model):
    researcher = models.ForeignKey(Researcher, default=1, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=10000, blank=True)
    description = models.TextField(blank=True)
    abstract = models.TextField(default='abstract', blank=True, null=True)
    list_date = models.CharField(max_length=1000)
    #listing_rating = models.IntegerField(default=1)
    research_paper = models.FileField(upload_to='research_papers/', blank=True)
    research_paper_txt = models.FileField(upload_to='research_papers/', blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(null=True, default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
# the main field to display is 'title'
    def __str__(self):
        return self.title
