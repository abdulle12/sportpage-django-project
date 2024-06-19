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
def home_articlee(request):
    return render(request,'home-article-5.html')
def home_articlef(request):
    return render(request,'home-article-6.html')
def home_articleg(request):
    return render(request,'home-article-7.html')
def home_articleh(request):
    return render(request,'home-article-8.html')
def newsa(request):
    return render(request,'News-article/news-article-1.html')
def newsb(request):
    return render(request,'News-article/news-article-2.html')
def newsc(request):
    return render(request,'News-article/news-article-3.html')
def newsd(request):
    return render(request,'News-article/news-article-4.html')
def newse(request):
    return render(request,'News-article/news-article-5.html')
def newsf(request):
    return render(request,'News-article/news-article-9.html')
def tranfera(request):
    return render(request, 'transfers-article/tranfer-article-1.html')

def tranferb(request):
    return render(request, 'transfers-article/tranfer-article-2.html')

def tranferc(request):
    return render(request, 'transfers-article/tranfer-article-3.html')

def tranferd(request):
    return render(request, 'transfers-article/tranfer-article-4.html')

def tranfere(request):
    return render(request, 'transfers-article/tranfer-article-5.html')

def tranferf(request):
    return render(request, 'transfers-article/tranfer-article-6.html')

def tranferg(request):
    return render(request, 'transfers-article/tranfer-article-7.html')

def tranferh(request):
    return render(request, 'transfers-article/tranfer-article-8.html')

def tranferi(request):
    return render(request, 'transfers-article/tranfer-article-9.html')