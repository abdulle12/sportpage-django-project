# sportapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('transfer/',views.transfer,name='transfer'),
    path('livescore/',views.livescore,name='livescore'),
    path('about/',views.about,name='about')
]
