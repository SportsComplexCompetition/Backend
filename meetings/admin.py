from django.contrib import admin
from .models import Meeting, Comment



admin.site.register(Comment)
admin.site.register(Meeting)