from django.db import models

# Create your models here.
class Banner(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    image = models.URLField(max_length=500) 
    
    

