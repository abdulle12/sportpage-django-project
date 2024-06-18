# sportapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def transfer(request):
    return render(request,'transfer.html')

def livescore(request):
    return render(request,'livescore.html')
def about(request):
    return render(request,'about.html')

def home_articlea(request):
    return render(request,'home-article-1.html')
def home_articleb(request):
    return render(request,'home-article-2.html')
def home_articlec(request):
    return render(request,'home-article-3.html')
def home_articled(request):
    return render(request,'home-article-4.html')