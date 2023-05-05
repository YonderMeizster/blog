from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
