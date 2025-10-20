from django.db import models

from apps.common.models import BaseModel

class School(BaseModel):
    school_number = models.CharField(max_length=100)
    girls_number = models.IntegerField()
    boys_number = models.IntegerField()
    teachers_number = models.IntegerField()
    
    def __str__(self):
        return self.school_number

class District(BaseModel):
    district = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.district

class Region(BaseModel):
    region = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.region