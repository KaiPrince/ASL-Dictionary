"""
* Project Name: ASL Dictionary
* File Name: optimize_videos.py
* Programmer: Kai Prince
* Date: Thu, Apr 23, 2020
* Description: This file contains a management command to optimize videos.
"""


from django.core.management.base import BaseCommand

from video_processor.service import maybe_convert_video_from_video
from asl_dictionary.models import SignVideo


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
            if not options["all"] and video.optimized_video_file:
                continue

            self.stdout.write(f"Generating optimized version for {video}...", ending="")
            self.stdout.flush()
            maybe_convert_video_from_video(video)
            video.save()
            self.stdout.write("Done")
