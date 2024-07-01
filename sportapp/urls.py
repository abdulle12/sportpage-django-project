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
    path('home-article-9/',views.home_articleg,name='home-article-9'),
    path('news-article-1/',views.newsa,name='news-article-1'),
    path('news-article-2/',views.newsb,name='news-article-2'),
    path('news-article-3/',views.newsc,name='news-article-3'),
    path('news-article-4/',views.newsd,name='news-article-4'),
    path('news-article-5/',views.newse,name='news-article-5'),
    path('news-article-6/',views.newsg,name='news-article-6'),
    path('news-article-9/',views.newsf,name='news-article-9'),
    path('news-article-7/',views.newsh,name='news-article-7'),
    path('news-article-8/',views.newsi,name='news-article-8'),
    path('tranfer-article-1/', views.tranfera, name='tranfer-article-1'),
    path('tranfer-article-2/', views.tranferb, name='tranfer-article-2'),
    path('tranfer-article-3/', views.tranferc, name='tranfer-article-3'),
    path('tranfer-article-4/', views.tranferd, name='tranfer-article-4'),
    path('tranfer-article-5/', views.tranfere, name='tranfer-article-5'),
    path('tranfer-article-6/', views.tranferf, name='tranfer-article-6'),
    path('tranfer-article-7/', views.tranferg, name='tranfer-article-7'),
    path('tranfer-article-8/', views.tranferh, name='tranfer-article-8'),
    path('tranfer-article-9/', views.tranferi, name='tranfer-article-9'),
    
    

    
    
]
