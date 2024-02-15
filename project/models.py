from django.db import models

# Create your models here.

class Project(models.Model):
    project_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=10000)
    desc = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='project/media')
    skil = models.CharField(max_length=10000)
    githubLinkFrontend = models.CharField(max_length=100)
    githubLinkBAckend = models.CharField(max_length=1000)
    backendLink = models.CharField(max_length=1000)
    frontendLink = models.CharField(max_length=1000)


    
