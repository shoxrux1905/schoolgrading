from django.db import models

from apps.common.models import BaseModel

class Chapter(BaseModel):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self): 
        return f"{self.title}"
    

class Subject(BaseModel):
    chapter=models.ManyToManyField(Chapter, blank=True)
    name = models.CharField(max_length=100)
    total_lessons = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.name}"


class Grade(BaseModel):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null= True)
    color = models.CharField(max_length=20, blank=True, null = True)
    order = models.PositiveIntegerField(default=0)
    subject = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.title