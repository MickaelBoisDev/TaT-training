# media_serializer.py
from rest_framework import serializers
from ..models.media import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
