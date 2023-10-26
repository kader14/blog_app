from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from .forms import CommentForm
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

from django.views.decorators.http import require_GET, require_POST

# Create your views here.

def list_of_articles(request, tag_slug= None):
    articles =Article.publishedArticles.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag])
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page', 1)
    try:
        articles = paginator.page(page_number)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles = paginator.page(1)
    return render(request , 'blog/list.html', {'articles' : articles, 'tag': tag})
    pass


def article_details(request,article):
    try:
        article = get_object_or_404(Article, status=Article.Status.PUBLISHED,
                                    slug= article)
        # List of active comments for this article
        comments = article.comments.filter(active=True)
        # Form for users to write comment
        form = CommentForm()
    except Article.DoesNotExist:
        raise Http404("لا توجد أي مقالة")   
    return render(request, 'blog/detail.html', {'article': article, 'comments': comments,'form': form})
    pass


@require_POST
def comment_for_article(request, article_id):

    # get the article by article_id
    article = get_object_or_404(Article, id = article_id, status=Article.Status.PUBLISHED)
    comment = None
    
    # A comment form
    form = CommentForm(data=request.POST)

    if form.is_valid():
        # Create a Comment object before saving it to the database
        comment = form.save(commit=False)

        # Assign the article to the comment
        comment.article = article
        # Save the comment to the database
        comment.save()
        pass

    return render(request, 'blog/comment.html', {'article': article, 'form': form, 'comment': comment})

    pass
