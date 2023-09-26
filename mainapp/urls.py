from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='all-articles'),
    path('articles/<int:pk>/', views.article_by_pk, name='article-by-pk'),
    path('all_categories', views.all_categories, name='all_categories')
]
