from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article, Category



def all_articles(request):
    articles = Article.objects.all()
    data = [{"title": article.title, "description": article.description, "image": article.image, "category": article.category} for article in articles]
    return JsonResponse(data, safe=False)




def article_by_pk(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = {"title": article.title, "description": article.description, "image": article.image, "category": article.category, "reading_time": article.reading_time}
    return JsonResponse(data)


def all_categories(request):
    articles = Category.objects.all()
    data = [{"category_name": article.category_name, "category_image": article.category_image} for article in articles]
    return JsonResponse(data, safe=False)