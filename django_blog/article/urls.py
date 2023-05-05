from django.urls import path
from django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:id>/', views.ArticleView.as_view(), name="article_id"),
]
