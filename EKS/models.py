from django.db import models

# Create your models here.

class Cluster(models.Model):
    email = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    nodes = models.IntegerField()
    vcpu = models.IntegerField()
    ram = models.IntegerField()
    #create_date = models.DateTimeField()

