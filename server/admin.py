# models/admin.py
from django.contrib import admin
from .models.media import Media

admin.site.register(Media)
