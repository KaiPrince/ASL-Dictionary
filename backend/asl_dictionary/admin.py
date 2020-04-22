"""
* Project Name: ASL Dictionary
* File Name: admin.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains admin registration for the ASL Dictionary app.
"""

from django.contrib import admin
from video_processor.service import generate_thumbnail, maybe_convert_video
from .models import SignImage, SignVideo, SignWord


class SignVideoAdmin(admin.ModelAdmin):
    """ Admin for SignVideo """

    def save_model(self, request, obj, form, change):
        if change and form.files.get("video_file"):
            preferred_ext = "webm"
            maybe_convert_video(
                obj.optimized_video_file, form.files.get("video_file"), preferred_ext
            )
            generate_thumbnail(obj.thumbnail_file, form.files.get("video_file"))

        return super().save_model(request, obj, form, change)


admin.site.register(SignWord)
admin.site.register(SignImage)
admin.site.register(SignVideo, SignVideoAdmin)
