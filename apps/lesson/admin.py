from django.contrib import admin

from apps.lesson.models import Chapter, Subject, Grade

admin.site.register(Chapter)
admin.site.register(Subject)
admin.site.register(Grade)