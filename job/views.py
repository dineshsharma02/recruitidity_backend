from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from .models import Job
from .serializers import JobListSerializer, JobCreateSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsEmployer

# Create your views here.


class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [IsAuthenticated]




class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer
    permission_classes = [IsAuthenticated,IsEmployer]

    def perform_create(self,serializer):
        serializer.save(posted_by=self.request.user)


class YourPostedJobsView(ListAPIView):
    serializer_class = JobListSerializer
    permission_classes = [IsAuthenticated,IsEmployer]
    
    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(posted_by = user)