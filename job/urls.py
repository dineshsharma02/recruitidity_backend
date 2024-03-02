from django.urls import path
from .views import JobCreateView,JobListView

app_name = 'job'

urlpatterns = [
    path('view-jobs/',JobListView.as_view(),name='job_list_api'),
    path('create-job/',JobCreateView.as_view(),name='job_create_api'),
]
