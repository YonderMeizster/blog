from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    return render(request, "article/index.html", context={'app_name': f"{__package__.split('.')[1]}"})
