from django.db import models

# Create your models here.


class sos(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    message = models.TextField(null=True)
    