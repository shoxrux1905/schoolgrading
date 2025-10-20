from rest_framework import serializers
from apps.AboutUs.models import VideoSection

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = ['id', 'videos', 'description', 'created_at', 'updated_at']