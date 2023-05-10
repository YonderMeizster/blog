from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Article
from .forms import CreateArticle


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={'articles': articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={'article': article})


class CreateArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CreateArticle()
        return render(request, 'article/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateArticle(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('create_article'))

        return render(request, 'article/create.html',  context={'form': form})


class UpdateArticleView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = CreateArticle(instance=article)
        return render(request, 'article/update.html', context={
            'form': form,
            'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = CreateArticle(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect(reverse('articles'))

        return render(request, 'articles/update.html', {'form' : form, 'article_id':article_id})
