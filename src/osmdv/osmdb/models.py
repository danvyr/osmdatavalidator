# from django.db import models
from django.contrib.gis.db import models


# Create your models here.

class Relation(models.Model):
    id = models.IntegerField()
    uid = models.IntegerField()
    changeset = models.IntegerField()
    version = models.IntegerField()
    user = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now=False, auto_now_add=False)
    tag = models.CharField()
    
    
class Node(models.Model):
    id = models.IntegerField()
    uid = models.IntegerField()
    changeset = models.IntegerField()
    version = models.IntegerField()
    user = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now=False, auto_now_add=False)
    tag = models.CharField()
    lat = models.IntegerField()
    lon = models.IntegerField()
    

class Way(models.Model):
    id = models.IntegerField()
    uid = models.IntegerField()
    changeset = models.IntegerField()
    version = models.IntegerField()
    user = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now=False, auto_now_add=False)
    tag = models.CharField()



    
