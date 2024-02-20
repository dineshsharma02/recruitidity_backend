from django.contrib import admin

from user.models import CustomUser
from job.models import Job
from application.models import Application
from application.models import Category

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Category)
