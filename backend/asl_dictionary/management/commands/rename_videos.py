"""
* Project Name: ASL Dictionary
* File Name: rename_videos.py
* Programmer: Kai Prince
* Date: Thu, Apr 23, 2020
* Description: This file contains a management command to rename videos.
"""

import ffmpeg
from django.core.management.base import BaseCommand
from django.utils.termcolors import colorize

from asl_dictionary.models import SignVideo
from video_processor.service import (
    save_file_to_storage,
    get_output_file_name,
    get_file_ext,
)


def rename_file(input_file, new_name):
    ext = input_file.name.rsplit(".", 1)[-1]
    file_name = new_name + "." + ext
    return file_name


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Do not skip files with existing entries.",
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):

        videos = SignVideo.objects.all()
        for video in videos:
            video_file = video.video_file
            new_name = rename_file(video_file, video.alt_text)

            if not options["all"] and video_file.name == new_name:
                continue

            self.stdout.write(f"Renaming {video}...", ending="")
            self.stdout.flush()
            try:
                video_file.name = new_name
                output_name = get_output_file_name(video_file, get_file_ext(video_file))
                save_file_to_storage(video_file, video_file, output_name)
                video.save()

            except ffmpeg.Error:
                self.stdout.write(colorize("Error", fg="red"))
            else:
                self.stdout.write(colorize("Done", fg="green"))
