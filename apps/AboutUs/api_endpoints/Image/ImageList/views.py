from rest_framework import generics

from apps.AboutUs.models import ImageSection
from apps.AboutUs.api_endpoints.Image.ImageList.serializers import ImageSerializer

class ImageListView(generics.RetrieveAPIView):
    queryset = ImageSection.objects.all()
    serializer_class = ImageSerializer
    
__all__ = ['ImageListView']