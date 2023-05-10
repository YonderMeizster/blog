from django.urls import path
from django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:id>/', views.ArticleView.as_view(), name="article_id"),
    path('create/', views.CreateArticleView.as_view(), name="create_article"),
]
