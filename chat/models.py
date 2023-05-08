from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.Charfield(max_lenght=500)
    
