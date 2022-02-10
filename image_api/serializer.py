from dataclasses import field, fields
import imp
from rest_framework import serializers
from .models import Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'name']