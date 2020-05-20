"""
* Project Name: ASL Dictionary
* File Name: filters.py
* Programmer: Kai Prince
* Date: Mon, May 11, 2020
* Description: This file contains filters for Django Admin.
"""

from django.contrib import admin


class IsCompressedVideo(admin.SimpleListFilter):
    title = "compressed"
    parameter_name = "was_compressed"

    def lookups(self, request, model_admin):
        return (
            ("yes", "Yes"),
            ("no", "No"),
        )

    def queryset(self, request, queryset):

        if self.value() == "yes":
            # str(self.video_file.name).startswith("compressed")
            return queryset.filter(video_file__contains="compressed_")

        if self.value() == "no":
            return queryset.exclude(video_file__contains="compressed_")


class HasWord(admin.SimpleListFilter):
    title = "has word"
    parameter_name = "has_word"

    def lookups(self, request, model_admin):
        return (
            ("yes", "Yes"),
            ("no", "No"),
        )

    def queryset(self, request, queryset):

        if self.value() == "yes":
            has_words = queryset.filter(words__isnull=False)

            # Fix for duplicates appearing (I don't know why)
            has_words = has_words.distinct()

            return has_words

        if self.value() == "no":
            has_words = queryset.filter(words__isnull=True)

            # Fix for duplicates appearing (I don't know why)
            has_words = has_words.distinct()

            return has_words
