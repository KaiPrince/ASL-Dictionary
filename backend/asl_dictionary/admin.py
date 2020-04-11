"""
* Project Name: ASL Dictionary
* File Name: admin.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains admin registration for the ASL Dictionary app.
"""


from django.contrib import admin
from .models import SignWord, SignImage, SignVideo

admin.site.register(SignWord)
admin.site.register(SignImage)
admin.site.register(SignVideo)
