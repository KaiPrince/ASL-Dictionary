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

    def __str__(self):
        return self.label


class SignImage(models.Model):
    """ An image which demostrates how to sign a word. """

    caption = models.TextField()
    image_file = models.ImageField(upload_to="sign_images/")

    def __str__(self):
        return self.caption
