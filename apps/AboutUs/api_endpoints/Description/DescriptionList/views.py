from rest_framework import generics

from apps.AboutUs.models import DescriptionSection
from apps.AboutUs.api_endpoints.Description.DescriptionList.serializers import DescriptionSerializer

class DescriptionListAPIView(generics.ListAPIView):
    queryset = DescriptionSection.objects.all()
    serializer_class = DescriptionSerializer
    
__all__ = ['DescriptionListAPIView']