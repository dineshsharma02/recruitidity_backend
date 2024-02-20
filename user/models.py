from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    role_choices = [('employer','Employer'),('candidate','Candidate')]
    role = models.CharField(choices = role_choices,max_length = 20)
    company = models.CharField(max_length=255,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)


CustomUser.groups.related_name = 'custom_user_groups'
CustomUser.user_permissions.related_name = 'custom_user_permissions'


