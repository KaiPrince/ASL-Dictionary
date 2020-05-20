"""
* Project Name: ASL Dictionary
* File Name: forms.py
* Programmer: Kai Prince
* Date: Wed, Apr 29, 2020
* Description: This file contains forms for the Django Admin.
"""

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from asl_dictionary.models import SignVideo, SignWord


class SignVideoAdminForm(forms.ModelForm):
    """ Custom form for SignVideo Admin """

    words = forms.ModelMultipleChoiceField(
        queryset=SignWord.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(verbose_name="words", is_stacked=False),
    )

    class Meta:
        model = SignVideo
        fields = ["alt_text", "caption", "video_file", "thumbnail_file"]

    def __init__(self, *args, **kwargs):
        super(SignVideoAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["words"].initial = self.instance.signword_set.all()

    def save(self, commit=True):
        video = super(SignVideoAdminForm, self).save(commit=False)

        if commit:
            video.save()

        if video.pk:
            video.signword_set.set(self.cleaned_data["words"])
            self.save_m2m()

        return video
