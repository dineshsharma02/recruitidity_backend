from rest_framework import serializers
from .models import Job

class JobListSerializer(serializers.ModelSerializer):
    posted_by_username = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields = ['id','title','description','skills_required','created_at','posted_by','posted_by_username']

    def get_posted_by_username(self,obj):
        return obj.posted_by.username if obj.posted_by else None


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','description','skills_required','created_at']