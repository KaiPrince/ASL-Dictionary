"""
* Project Name: ASL Dictionary
* File Name: actions.py
* Programmer: Kai Prince
* Date: Wed, Apr 29, 2020
* Description: This file contains actions for the Django Admin.
"""

from django.contrib import messages

from asl_dictionary import tasks


def compress_video(_modeladmin, request, queryset):
    for obj in queryset:
        tasks.compress_video.delay(obj.id)
    messages.success(request, "Task started.")


def optimize_video(_modeladmin, request, queryset):
    for obj in queryset:
        tasks.optimize_video.delay(obj.id)
    messages.success(request, "Task started.")


def generate_thumbnail(_modeladmin, request, queryset):
    for obj in queryset:
        tasks.generate_thumbnail_from_video.delay(obj.id)
    messages.success(request, "Task started.")


def postprocess_video(_modeladmin, request, queryset):
    for obj in queryset:
        tasks.postprocess_video.delay(obj.id)
    messages.success(request, "Task started.")


def mark_as_sentence(_modeladmin, _request, queryset):
    for obj in queryset:
        obj.is_sentence = True
        obj.save()
