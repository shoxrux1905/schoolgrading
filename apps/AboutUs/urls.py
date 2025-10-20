from django.urls import path

from apps.AboutUs.api_endpoints import DescriptionListAPIView, ImageListView, VideoListView

urlpatterns = [
    path('DescriptionSection/', DescriptionListAPIView.as_view(), name='description-section-list'),
    path('ImageSection/<int:pk>/', ImageListView.as_view(), name='image-section-detail'),
    path('VideoSection/<int:pk>/', VideoListView.as_view(), name='video-section-detail'),
]
