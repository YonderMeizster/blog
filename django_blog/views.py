from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={
            'who': 'World',
        })


def about(request):
    return render(request, 'about.html')
