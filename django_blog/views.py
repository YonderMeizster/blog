from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'article_id': 42, 'tags': 'python'}))

        return render(request, 'index.html', context={
            'who': 'World',
        })


def about(request):
    return render(request, 'about.html')
