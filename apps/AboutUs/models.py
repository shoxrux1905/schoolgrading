from django.db import models

from apps.common.models import BaseModel

class DescriptionSection(BaseModel):
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.description[:50]  

class ImageSection(BaseModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='about_us_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class VideoSection(BaseModel):
    description = models.CharField(max_length=500)
    videos = models.FileField(upload_to='about_us_videos/', null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description[:50]
    
    
    