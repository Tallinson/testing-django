from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

# Create your views here.


def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    return render(request, 'articles/article_create.html')
