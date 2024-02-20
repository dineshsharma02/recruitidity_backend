from django.db import models

from job.models import Job
from user.models import CustomUser

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Application(models.Model):
    candidate_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    applied_for = models.ForeignKey(Job,on_delete = models.CASCADE)
    submitted_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    status_choices = [('pending','Pending'),('accepted','Accepted'),('rejected','Rejected')]
    status = models.CharField(choices = status_choices,default='pending',max_length=20)

    # fields for nlp 

    relevance_score = models.FloatField(default=0.0)

    #custom categories for specific job
    custom_categories = models.ManyToManyField(Category)


