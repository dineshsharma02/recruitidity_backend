from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from .models import Job
from .serializers import JobSerializer

# Create your views here.


class JobListCreateView(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self,serializer):
        serializer.save(posted_by=self.request.user)

