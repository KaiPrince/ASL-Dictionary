"""
* Project Name: ASL Dictionary
* File Name: generate_thumbnails.py
* Programmer: Kai Prince
* Date: Thu, Apr 23, 2020
* Description: This file contains a management command to generate thumbnails.
"""

from django.core.management.base import BaseCommand

from asl_dictionary.models import SignVideo
from video_processor.service import generate_thumbnail_from_video


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
            if not options["all"] and video.thumbnail_file:
                continue

            self.stdout.write(f"Generating thumbnail for {video}...", ending="")
            self.stdout.flush()
            generate_thumbnail_from_video(video)
            video.save()
            self.stdout.write("Done")
