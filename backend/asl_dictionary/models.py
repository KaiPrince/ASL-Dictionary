"""
* Project Name: ASL Dictionary
* File Name: models.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains models for the asl_dictionary app.
"""

from django.db import models


class SignWord(models.Model):
    """ A word in ASL, such as 'Hello'. """

    class Meta:
        ordering = ["-id"]

    label = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField("SignImage", blank=True)
    videos = models.ManyToManyField("SignVideo", blank=True)
    see_also = models.ManyToManyField("SignWord", blank=True, symmetrical=True)

    def __str__(self):
        return self.label


class MediaResource(models.Model):
    """ An image or video. """

    class Meta:
        abstract = True

    alt_text = models.CharField(
        unique=True,
        max_length=50,
        help_text="Textual representation of the image. Used by screen-readers and when the image is unavailable.",
    )
    caption = models.TextField(help_text="Displayed alongside the image.")

    def __str__(self):
        return self.alt_text


class SignImage(MediaResource):
    """ An image which demostrates how to sign a word. """

    image_file = models.ImageField(upload_to="sign_images/")


class SignVideo(MediaResource):
    """ A video which demonstrates how to sign a word. """

    video_file = models.FileField(upload_to="sign_videos/")
