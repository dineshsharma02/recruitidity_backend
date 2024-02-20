from django.urls import path
from .views import JobListCreateView

app_name = 'job'

urlpatterns = [
    path('api/',JobListCreateView.as_view(),name='job_list_create_api'),
]
