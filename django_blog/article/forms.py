from django.forms import ModelForm
from .models import Article


class CreateArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
