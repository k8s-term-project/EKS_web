from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cluster(models.Model):
    #email = models.CharField(max_length=100)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    master_num = models.IntegerField()
    master_cpu = models.IntegerField()
    master_ram = models.IntegerField()
    master_disk = models.IntegerField()
    node_num = models.IntegerField()
    node_cpu = models.IntegerField()
    node_ram = models.IntegerField()
    node_disk = models.IntegerField()

