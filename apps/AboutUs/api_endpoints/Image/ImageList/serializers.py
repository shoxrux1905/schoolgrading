from rest_framework import serializers

from apps.AboutUs.models import ImageSection

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSection
        fields = ['id', 'image', 'description', 'created_at', 'updated_at']