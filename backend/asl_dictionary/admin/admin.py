"""
* Project Name: ASL Dictionary
* File Name: admin.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains admin registration for the ASL Dictionary app.
"""
from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple


from asl_dictionary.admin.actions import (
    compress_video,
    generate_thumbnail,
    optimize_video,
    postprocess_video,
    mark_as_sentence,
)
from asl_dictionary.models import SignImage, SignVideo, SignWord

from asl_dictionary.admin.filters import IsCompressedVideo, HasWord

from asl_dictionary import tasks


class SignVideoAdmin(admin.ModelAdmin):
    """ Admin for SignVideo """

    actions = [
        postprocess_video,
        compress_video,
        optimize_video,
        generate_thumbnail,
        mark_as_sentence,
    ]

    formfield_overrides = {
        models.ManyToManyField: {
            "widget": FilteredSelectMultiple(verbose_name="words", is_stacked=False)
        },
    }

    search_fields = ["alt_text", "caption"]
    list_display = ("alt_text", "caption")
    list_filter = [IsCompressedVideo, HasWord, "is_sentence"]

    def save_model(self, request, obj, form, change):

        # Change file name to match alt_text
        input_file = form.files.get("video_file")
        if input_file:
            rename_file(input_file, obj.alt_text)
            rename_file(obj.video_file, obj.alt_text)

        # Save model
        super().save_model(request, obj, form, change)

        # Start background job
        tasks.postprocess_video.delay(obj.id)


class SignWordAdmin(admin.ModelAdmin):
    search_fields = ["label"]
    list_display = ("label", "synonyms", "description")


admin.site.register(SignWord, SignWordAdmin)
admin.site.register(SignImage)
admin.site.register(SignVideo, SignVideoAdmin)


def rename_file(input_file, new_name):
    ext = input_file.name.rsplit(".", 1)[-1]
    file_name = new_name + "." + ext
    input_file.name = file_name
