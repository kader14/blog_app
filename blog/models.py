from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    class ArticlePublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Article.Status.PUBLISHED)
            pass
        pass        

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250 , unique_for_date='publish')
    body =models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager() #The default manager
    publishedArticles = ArticlePublishedManager() #The custom manager
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        pass

    def __srt__(self):
        return self.title
        pass

    def get_canonical_url(self):
        return reverse('blog:aa',
        args= [
            self.slug
                ]
        )
        pass
    pass


