"""
* Project Name: ASL Dictionary
* File Name: views.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains Views for the ASL Dictionary app.
"""

from django.views import generic
from .models import SignWord


class IndexView(generic.ListView):
    model = SignWord
    template_name = "index.html"


class DetailView(generic.DetailView):
    model = SignWord
    template_name = "detail.html"

