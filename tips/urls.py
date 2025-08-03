from django.urls import path
from .views import article_list, article_detail, add_article, my_articles, edit_article, delete_article

urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:article_id>/', article_detail, name='article_detail'),
    path('add/', add_article, name='add_article'),
    path('my_articles/', my_articles, name='my_articles'),
    path('<int:article_id>/edit/', edit_article, name='edit_article'),
    path('<int:article_id>/delete/', delete_article, name='delete_article'),
]
