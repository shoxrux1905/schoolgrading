from rest_framework import serializers

from apps.AboutUs.models import DescriptionSection

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionSection
        fields = '__all__'