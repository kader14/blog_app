from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def list_of_articles(request):
    articles =Article.publishedArticles.all()
    #print (articles)
    return render(request , 'blog/list.html', {'articles' : articles})
    pass
    
