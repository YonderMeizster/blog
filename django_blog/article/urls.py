from django.urls import path
from django_blog.article import views


urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<str:tags>/<int:article_id>/', views.article_id, name="article")
]
