"""
* Project Name: ASL Dictionary
* File Name: postprocess_videos.py
* Programmer: Kai Prince
* Date: Wed, Apr 29, 2020
* Description: This file contains a management command to postprocess videos.
"""

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Do not skip files with existing entries.",
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        call_command("generate_thumbnails", *args, **options)
        call_command("optimize_videos", *args, **options)
        call_command("compress_videos", *args, **options)
