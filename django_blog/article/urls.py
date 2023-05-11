from django.urls import path
from django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', views.UpdateArticleView.as_view(), name='update_article'),
    path('<int:id>/', views.ArticleView.as_view(), name="article_id"),
    path('create/', views.CreateArticleView.as_view(), name="create_article"),
    path('<int:id>/delete/', views.DeleteArticleView.as_view(), name="delete_article"),
]
