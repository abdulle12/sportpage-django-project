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