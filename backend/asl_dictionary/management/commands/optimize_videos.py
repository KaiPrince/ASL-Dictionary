"""
* Project Name: ASL Dictionary
* File Name: optimize_videos.py
* Programmer: Kai Prince
* Date: Thu, Apr 23, 2020
* Description: This file contains a management command to optimize videos.
"""

import ffmpeg
from django.core.management.base import BaseCommand
from django.utils.termcolors import colorize

from asl_dictionary.models import SignVideo
from video_processor.service import optimize_video


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Do not skip files with existing entries.",
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        count_success = 0
        count_failure = 0

        videos = SignVideo.objects.all()
        for video in videos:
            if not options["all"] and video.optimized_video_file:
                continue

            self.stdout.write(f"Generating optimized version for {video}...", ending="")
            self.stdout.flush()
            try:
                optimize_video(video)
                video.save()

            except ffmpeg.Error:
                count_failure += 1
                self.stdout.write(colorize("Error", fg="red"))
            else:
                count_success += 1
                self.stdout.write(colorize("Done", fg="green"))

        self.stdout.write(
            colorize(f"Successfully processed {count_success} items.", fg="green")
        )
        if count_failure:
            self.stdout.write(
                colorize(f"Failed to process {count_failure} items.", fg="red")
            )
