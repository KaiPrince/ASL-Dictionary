"""
* Project Name: ASL Dictionary
* File Name: views.py
* Programmer: Kai Prince
* Date: Fri, Apr 10, 2020
* Description: This file contains Views for the ASL Dictionary app.
"""

from django.views import generic
from .models import SignWord, SignImage, SignVideo
from asl_webscraper.service import search_lifeprint, search_handspeak
from .serializers import SignWordSerializer, SignImageSerializer, SignVideoSerializer
from rest_framework import viewsets


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
            results = []
            results.extend(search_handspeak(query))
            results.extend(search_lifeprint(query))
            context["results"] = results

        return context

    def post(self, request):
        return self.get(request)


class SignWordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SignWord.objects.all()
    serializer_class = SignWordSerializer


class SignImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SignImage.objects.all()
    serializer_class = SignImageSerializer


class SignVideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SignVideo.objects.all()
    serializer_class = SignVideoSerializer
