"""
* Project Name: ASL Dictionary
* File Name: tasks.py
* Programmer: Kai Prince
* Date: Wed, May 20, 2020
* Description: This file contains background tasks.
"""

# Create your tasks here
from celery import shared_task, chain
from video_processor import service
from asl_dictionary.models import SignVideo


@shared_task
def postprocess_video(video_id):
    """ Performs background processing on a video. """
    spawn_children = chain(
        generate_thumbnail_from_video.si(video_id),
        optimize_video.si(video_id),
        compress_video.si(video_id),
    )

    spawn_children.delay()


@shared_task
def generate_thumbnail_from_video(video_id):
    """ Generates and saves a video thumbnail. """
    video = SignVideo.objects.get(pk=video_id)

    service.generate_thumbnail_from_video(video)
    video.save()


@shared_task
def optimize_video(video_id):
    """ Generates and saves a low-res scaled down video. """
    video = SignVideo.objects.get(pk=video_id)

    service.optimize_video(video)
    video.save()


@shared_task
def compress_video(video_id):
    """ Replaces current video with compressed version. """
    video = SignVideo.objects.get(pk=video_id)

    service.compress_video(video)
    video.save()
