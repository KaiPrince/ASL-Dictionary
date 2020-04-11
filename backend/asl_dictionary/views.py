"""
* Project Name: ASL Dictionary
* File Name: views.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains Views for the ASL Dictionary app.
"""

from django.views import generic
from .models import SignWord
from asl_webscraper.service import search_lifeprint


class IndexView(generic.ListView):
    model = SignWord
    template_name = "index.html"


class DetailView(generic.DetailView):
    model = SignWord
    template_name = "detail.html"


class SearchView(generic.TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query")
        if query:
            context["results"] = search_lifeprint(query)

        return context

    def post(self, request):
        return self.get(request)
