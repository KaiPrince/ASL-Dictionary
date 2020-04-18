"""
* Project Name: ASL Dictionary
* File Name: admin.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains admin registration for the ASL Dictionary app.
"""


import os

import ffmpeg
from django.contrib import admin
from django.core.files import File

from .models import SignImage, SignVideo, SignWord


class SignVideoAdmin(admin.ModelAdmin):
    """ Admin for SignVideo """

    def save_model(self, request, obj, form, change):
        if change and form.files.get("video_file"):
            preferred_ext = "webm"
            maybe_convert_video(
                obj.video_file, form.files.get("video_file"), preferred_ext
            )
            generate_thumbnail(obj.thumbnail_file, form.files.get("video_file"))

        return super().save_model(request, obj, form, change)


admin.site.register(SignWord)
admin.site.register(SignImage)
admin.site.register(SignVideo, SignVideoAdmin)


def get_video_file(in_memory_file):
    # write InMemoryFile to disk
    with open("temp_uploaded_file", "xb") as temp_file:
        for chunk in in_memory_file.chunks():
            temp_file.write(chunk)

    return File(open("temp_uploaded_file", "rb"))  # TODO close


def get_output_file_name(input_file, ext):
    file_path_name = input_file.name.rsplit(".", 1)[0]
    file_name = file_path_name.rsplit("/", 1)[-1] + "." + ext
    return file_name


def convert_video(input_file, ext):
    # ..Generate new file.
    temp_file_name = f"temp.{ext}"
    (ffmpeg.input(input_file).output(temp_file_name).run(overwrite_output=True))


def save_file_to_storage(file, read_file, output_name):
    # ..Save new file to storage
    with open(read_file, "rb") as raw_file:
        new_file = File(raw_file)
        file.save(output_name, new_file)


def cleanup_temp_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def maybe_convert_video(current_file, new_file_in_mem, preferred_ext):
    new_file_ext = new_file_in_mem.name.rsplit(".", 1)[-1]

    if new_file_ext != preferred_ext:
        cleanup_temp_files(["temp_uploaded_file", "temp.webm"])
        file = get_video_file(new_file_in_mem)

        # sign_videos/test.mp4 => test.webm
        file_name = get_output_file_name(new_file_in_mem, preferred_ext)

        # temp_uploaded_file
        temp_file_url = file.file.name

        convert_video(temp_file_url, preferred_ext)

        save_file_to_storage(current_file, "temp.webm", file_name)

        file.close()
        cleanup_temp_files(["temp_uploaded_file", "temp.webm"])


def generate_thumbnail(current_file, new_file_in_mem):
    cleanup_temp_files(["temp_uploaded_file", "temp.webp"])
    file = get_video_file(new_file_in_mem)

    # sign_videos/test.mp4 => test.webp
    file_name = get_output_file_name(new_file_in_mem, "webp")

    # temp_uploaded_file
    temp_file_url = file.file.name

    (
        ffmpeg.input(temp_file_url, ss="0:00")
        .filter("thumbnail")
        .output("temp.webp", vframes=1)
        .run(overwrite_output=True)
    )

    save_file_to_storage(current_file, "temp.webp", file_name)

    file.close()
    cleanup_temp_files(["temp_uploaded_file", "temp.webp"])
