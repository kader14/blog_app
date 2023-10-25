from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.list_of_articles , name="list_of_articles"),
    #path('<int:id>/', views.article_details, name="a"),
    path('<slug:article>/', views.article_details, name='aa'),
]
