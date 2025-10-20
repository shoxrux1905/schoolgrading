from django.contrib import admin

from apps.AboutUs.models import DescriptionSection, ImageSection, VideoSection

admin.site.register(DescriptionSection)
admin.site.register(ImageSection)
admin.site.register(VideoSection)