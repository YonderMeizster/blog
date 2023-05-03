from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "article/index.html", context={
            'app_name': f"{__package__.split('.')[1]}"
            })


def article_id(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
