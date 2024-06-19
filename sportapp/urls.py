# sportapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('transfer/',views.transfer,name='transfer'),
    path('livescore/',views.livescore,name='livescore'),
    path('about/',views.about,name='about'),
    path('home-article-1/',views.home_articlea,name='home-article-1'),
    path('home-article-2/',views.home_articleb,name='home-article-2'),
    path('home-article-3/',views.home_articlec,name='home-article-3'),
    path('home-article-4/',views.home_articled,name='home-article-4'),
    path('home-article-5/',views.home_articlee,name='home-article-5'),
    path('home-article-6/',views.home_articlef,name='home-article-6'),
    path('home-article-7/',views.home_articleg,name='home-article-7'),
    path('home-article-8/',views.home_articleh,name='home-article-8'),

    
    
]
