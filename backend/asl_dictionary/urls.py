"""
* Project Name: ASL Dictionary
* File Name: urls.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains the URLconf for the ASL Dictionary app.
"""

from django.urls import path

from . import views

app_name = "asl_dictionary"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
