"""
* Project Name: ASL Dictionary
* File Name: serializers.py
* Programmer: Kai Prince
* Date: Sat, Apr 11, 2020
* Description: This file contains serializers for the ASL Dictionary app.
"""

from rest_framework import serializers
from .models import SignWord, SignImage, SignVideo



class SignImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignImage
        fields = ["alt_text", "caption", "image_file"]


class SignVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignImage
        fields = ["alt_text", "caption", "video_file"]


class SignWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignWord
        fields = ["label", "description", "images", "videos"]

    images = SignImageSerializer(many=True)
    videos = SignVideoSerializer(many=True)
