"""
* Project Name: ASL Dictionary
* File Name: admin.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains admin registration for the ASL Dictionary app.
"""

from django.contrib import admin
from .models import SignImage, SignVideo, SignWord


class SignVideoAdmin(admin.ModelAdmin):
    """ Admin for SignVideo """

    def save_model(self, request, obj, form, change):
        # Change file name to match alt_text

        input_file = form.files.get("video_file")

        if change and input_file:
            rename_file(obj.video_file, obj.alt_text)
            rename_file(input_file, obj.alt_text)

        return super().save_model(request, obj, form, change)


admin.site.register(SignWord)
admin.site.register(SignImage)
admin.site.register(SignVideo, SignVideoAdmin)


def rename_file(input_file, new_name):
    ext = input_file.name.rsplit(".", 1)[-1]
    file_name = new_name + "." + ext
    input_file.name = file_name
