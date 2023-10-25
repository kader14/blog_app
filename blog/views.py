from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def list_of_articles(request):
    articles =Article.publishedArticles.all()
    #print (articles)
    return render(request , 'blog/list.html', {'articles' : articles})
    pass


def article_details(request,article):
    try:
        article = get_object_or_404(Article, status=Article.Status.PUBLISHED,
                                    slug= article)
    except Article.DoesNotExist:
        raise Http404("لا توجد أي مقالة")   
    return render(request, 'blog/detail.html', {'article': article})
    pass

