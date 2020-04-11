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

    label = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField("SignImage")
    videos = models.ManyToManyField("SignVideo")

    def __str__(self):
        return self.label


class MediaResource(models.Model):
    """ An image or video. """

    class Meta:
        abstract = True

    caption = models.TextField()

    def __str__(self):
        return self.caption


class SignImage(MediaResource):
    """ An image which demostrates how to sign a word. """

    image_file = models.ImageField(upload_to="sign_images/")


class SignVideo(MediaResource):
    """ A video which demonstrates how to sign a word. """

    video_file = models.FileField(upload_to="sign_videos/")
