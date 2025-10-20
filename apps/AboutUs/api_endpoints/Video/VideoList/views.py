from rest_framework import generics

from apps.AboutUs.models import VideoSection
from apps.AboutUs.api_endpoints.Video.VideoList.serializers import VideoSerializer

class VideoListView(generics.RetrieveAPIView):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSerializer
    
__all__ = ['VideoListView']