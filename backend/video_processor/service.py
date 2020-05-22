"""
* Project Name: ASL Dictionary
* File Name: service.py
* Programmer: Kai Prince
* Date: Wed, Apr 22, 2020
* Description: This file contains service functions for the Video Processor app.
"""


import os
import sys

import ffmpeg
from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage

from asl_dictionary.models import SignVideo


def generate_thumbnail_from_video(video: SignVideo):
    """ Generates a thumbnail image from a video and uploads to the storage system. """
    output_ext = "jpg"

    (input_file, local_file, output_name) = get_file_names(video.video_file, output_ext)

    try:
        generate_thumbnail(input_file, local_file)
    except ffmpeg.Error as err:
        try:
            sys.stderr.buffer.write(err.stderr)
        except AttributeError:
            # Docker uses a 'LoggingProxy' object, which does not have a buffer.
            sys.stderr.write(err.stderr)
        raise err

    upload_to_storage(video.thumbnail_file, local_file, output_name, overwrite=True)


def optimize_video(video: SignVideo):
    """ Generates a even smaller size video, and saves as new video_file. """
    ext = get_file_ext(video.video_file)
    (input_file, local_file, output_name) = get_file_names(video.video_file, ext)

    try:
        generate_optimized_video(input_file, local_file)
    except ffmpeg.Error as err:
        try:
            sys.stderr.buffer.write(err.stderr)
        except AttributeError:
            # Docker uses a 'LoggingProxy' object, which does not have a buffer.
            sys.stderr.write(err.stderr)

        raise err

    upload_to_storage(
        video.optimized_video_file, local_file, output_name, overwrite=True
    )


def compress_video(video: SignVideo):
    """ Generates a smaller size video, and overwrites current video_file. """
    ext = get_file_ext(video.video_file)
    (input_file, local_file, output_name) = get_file_names(video.video_file, ext)

    try:
        generate_compressed_video(input_file, local_file)
    except ffmpeg.Error as err:
        try:
            sys.stderr.buffer.write(err.stderr)
        except AttributeError:
            # Docker uses a 'LoggingProxy' object, which does not have a buffer.
            sys.stdout.write(err.stderr)
        raise err

    output_name = "compressed_" + output_name
    upload_to_storage(video.video_file, local_file, output_name, overwrite=True)


def rename_video(video: SignVideo):
    """ Saves file as new video file. """
    ext = get_file_ext(video.video_file)
    (_input_file, local_file, output_name) = get_file_names(video, ext)

    upload_to_storage(video.video_file, local_file, output_name)


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


def get_file_ext(video_file):
    ext = video_file.name.rsplit(".", 1)[-1]
    return ext


def get_file_names(video_file: File, ext: str):
    """ Consumes a video and string, and produces three strings. """
    temp_file_url = get_file_url(video_file)
    temp_output_file = f"temp.{ext}"

    file_name = get_output_file_name(video_file, ext)

    return (temp_file_url, temp_output_file, file_name)


def generate_thumbnail(input_url, output_file_name):
    (
        ffmpeg.input(input_url)
        .video.filter("scale", w=-2, h=360)
        .filter("thumbnail")
        .output(output_file_name, vframes=1)
        .overwrite_output()
        .run(quiet=True)
    )


def generate_optimized_video(input_file, output_file_name):
    (
        ffmpeg.input(input_file)
        .video.filter("scale", w=-2, h=360)
        .output(output_file_name, crf=24, vcodec="h264")
        .overwrite_output()
        .run(quiet=True)
    )


def generate_compressed_video(input_file, output_file_name):
    (
        ffmpeg.input(input_file)
        .video.output(output_file_name, crf=24, vcodec="h264")
        .overwrite_output()
        .run(quiet=True)
    )


def upload_to_storage(storage_file, local_file, file_name, overwrite=False):
    # I think the django-cleanup app is doing this for me.
    if (
        overwrite
        and not settings.IN_PRODUCTION
        and storage_file.name
        and default_storage.exists(storage_file.name)
    ):
        default_storage.delete(storage_file.name)

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
