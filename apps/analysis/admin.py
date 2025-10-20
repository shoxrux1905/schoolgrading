from django.contrib import admin

from apps.analysis.models import School, District, Region

admin.site.register(School)
admin.site.register(District)
admin.site.register(Region)
