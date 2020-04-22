"""
* Project Name: ASL Dictionary
* File Name: service.py
* Programmer: Kai Prince
* Date: Wed, Apr 22, 2020
* Description: This file contains service functions for the Video Processor app.
"""


import os

import ffmpeg
from django.core.files import File


def get_video_file(in_memory_file, temp_uploaded_file):
    # write InMemoryFile to disk
    with open(temp_uploaded_file, "xb") as temp_file:
        for chunk in in_memory_file.chunks():
            temp_file.write(chunk)

    return File(open(temp_uploaded_file, "rb"))


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
        temp_output_file = f"temp.{preferred_ext}"
        temp_uploaded_file = f"temp_uploaded_file.{new_file_ext}"
        cleanup_temp_files([temp_uploaded_file, temp_output_file])
        file = get_video_file(new_file_in_mem, temp_uploaded_file)

        # sign_videos/test.mp4 => test.webm
        file_name = get_output_file_name(new_file_in_mem, preferred_ext)

        # temp_uploaded_file
        temp_file_url = file.file.name

        convert_video(temp_file_url, preferred_ext)

        save_file_to_storage(current_file, temp_output_file, file_name)

        file.close()
        cleanup_temp_files([temp_uploaded_file, temp_output_file])


def generate_thumbnail(current_file, new_file_in_mem):
    new_file_ext = new_file_in_mem.name.rsplit(".", 1)[-1]
    preferred_ext = "jpg"

    temp_output_file = f"temp.{preferred_ext}"
    temp_uploaded_file = f"temp_uploaded_file.{new_file_ext}"

    cleanup_temp_files([temp_uploaded_file, temp_output_file])

    file = get_video_file(new_file_in_mem, temp_uploaded_file)

    # sign_videos/test.mp4 => test.webp
    file_name = get_output_file_name(new_file_in_mem, preferred_ext)

    # temp_uploaded_file
    temp_file_url = file.file.name

    (
        ffmpeg.input(temp_file_url, ss="0:00")
        .filter("thumbnail")
        .output(temp_output_file, vframes=1)
        .run(overwrite_output=True)
    )

    save_file_to_storage(current_file, temp_output_file, file_name)

    file.close()
    cleanup_temp_files([temp_uploaded_file, temp_output_file])
