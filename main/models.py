from django.db import models

# Create your models here.

class Movie(models.Model):
    # Fields for the movie table
    name=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    cast=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)
    release_date=models.DateField()
    avearge_rating=models.FloatField(default=0)
    image=models.URLField(default = None,null = True)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    