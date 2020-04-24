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
from django.conf import settings

from asl_dictionary.models import SignVideo


def generate_thumbnail_from_video(video: SignVideo):
    """ Generates a thumbnail image from a video and uploads to the storage system. """
    output_ext = "jpg"

    (input_file, local_file, output_name) = get_file_names(video, output_ext)

    generate_thumbnail(input_file, local_file)

    upload_to_storage(video.thumbnail_file, local_file, output_name)


def maybe_convert_video_from_video(video: SignVideo):
    """ Generates an optimized video and uploads to the storage system. """
    output_ext = "webm"

    ext = video.video_file.name.rsplit(".", 1)[-1]
    if ext != output_ext:
        (input_file, local_file, output_name) = get_file_names(video, output_ext)

        generate_optimized_video(input_file, local_file)

        upload_to_storage(video.optimized_video_file, local_file, output_name)


def get_output_file_name(input_file, ext):

    # sign_videos/test.mp4 => test.jpg
    file_path_name = input_file.name.rsplit(".", 1)[0]
    file_name = file_path_name.rsplit("/", 1)[-1] + "." + ext
    return file_name


def get_file_url(video_file):
    output = (
        video_file.url
        if settings.IN_PRODUCTION
        else settings.MEDIA_URL + video_file.name
    )
    if output.startswith("/"):
        output = output.strip("/")

    return output


def get_file_names(video: SignVideo, ext: str):
    """ Consumes a video and string, and produces three strings. """
    video_file = video.video_file
    temp_file_url = get_file_url(video_file)
    temp_output_file = f"temp.{ext}"

    file_name = get_output_file_name(video_file, ext)

    return (temp_file_url, temp_output_file, file_name)


def generate_thumbnail(input_url, output_file_name):
    (
        ffmpeg.input(input_url)
        .filter("thumbnail")
        .output(output_file_name, vframes=1)
        .run(overwrite_output=True, capture_stderr=True)
    )


def generate_optimized_video(input_file, output_file_name):
    # ..Generate new file.
    (
        ffmpeg.input(input_file)
        .output(output_file_name)
        .run(overwrite_output=True, capture_stderr=True)
    )


def upload_to_storage(storage_file, local_file, file_name):
    save_file_to_storage(storage_file, local_file, file_name)
    cleanup_temp_files([local_file])


def save_file_to_storage(file, read_file, output_name):
    # ..Save new file to storage
    with open(read_file, "rb") as raw_file:
        new_file = File(raw_file)
        file.save(output_name, new_file)


def cleanup_temp_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
