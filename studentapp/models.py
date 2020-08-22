from django.db import models

# Create your models here.

class stdmodel(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    course = models.CharField(max_length=256)
