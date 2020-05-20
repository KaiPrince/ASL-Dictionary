"""
* Project Name: ASL Dictionary
* File Name: actions.py
* Programmer: Kai Prince
* Date: Wed, Apr 29, 2020
* Description: This file contains actions for the Django Admin.
"""

from django.contrib import messages

from video_processor import service


def compress_video(_modeladmin, request, queryset):
    for obj in queryset:
        service.compress_video(obj)
        obj.save()
    messages.success(request, "Video(s) processed successfully.")


def optimize_video(_modeladmin, request, queryset):
    for obj in queryset:
        service.optimize_video(obj)
        obj.save()
    messages.success(request, "Video(s) processed successfully.")


def generate_thumbnail(_modeladmin, request, queryset):
    for obj in queryset:
        service.generate_thumbnail_from_video(obj)
        obj.save()
    messages.success(request, "Video(s) processed successfully.")


def postprocess_video(_modeladmin, request, queryset):
    for video in queryset:
        service.generate_thumbnail_from_video(video)
        service.optimize_video(video)
        service.compress_video(video)
        video.save()
    messages.success(request, "Video(s) processed successfully.")
