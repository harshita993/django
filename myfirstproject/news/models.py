from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class News(models.Model):
    news_title =models.CharField(max_length=50)
    news_description = HTMLField()
    news_slug=AutoSlugField(populate_from="news_title" ,unique=True,null=True,default=None)
    
    

