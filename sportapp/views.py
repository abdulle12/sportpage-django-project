# sportapp/views.py
from django.shortcuts import render
from .models import Homepage
from .models import Homepage1
from .models import Homepage2
from .models import Homepage3
from .models import Newspage1
from .models import Newspage2
from .models import Newspage3
from .models import Newspage4
from .models import Transfepage1
from .models import Transfepage2
from .models import Transfepage3
from .models import Transfepage4
from .models import League
from datetime import datetime
from .models import Home_article_1,Home_article_2,Home_article_3
from .models import Home_article_4,Home_article_5,Home_article_6,Home_article_7
from .models import Home_article_8,Home_article_9,News_article_1,News_article_2
from .models import News_article_3,News_article_4,News_article_5,News_article_6
from .models import News_article_7,News_article_8,News_article_9
from .models import Transfer_article_1,Transfer_article_2,Transfer_article_3,Transfer_article_4,Transfer_article_5
from .models import Transfer_article_6








def index(request):
    
    


    
   
    articles=Homepage.objects.all()
    showcasesa=Homepage2.objects.all()
    showcases=Homepage1.objects.all()
    articlesa=Homepage3.objects.all()
    articlesa=Homepage3.objects.all()
    context = {
        'articles': articles,
        'showcases': showcases,
        'showcasesa':showcasesa,
        'articlesa': articlesa,

    }

    
    return render(request, 'index.html', context)




#news page views
def news(request):
    articles=Newspage1.objects.all()
    articlesa=Newspage2.objects.all()
    articlesb=Newspage3.objects.all()
    last=Newspage4.objects.all()

    context = {
        'articles': articles,
        'articlesa': articlesa,
        'articlesb': articlesb,
        'last': last,
        

    }
    
    return render(request, 'news.html',context)



def transfer(request):
    articles=Transfepage1.objects.all()
    articlesa=Transfepage2.objects.all()
    articlesb=Transfepage3.objects.all()
    articlesc=Transfepage4.objects.all()

    
    context = {
        'articles': articles,
        'articlesa': articlesa,
        'articlesb': articlesb,
        'articlesc': articlesc,
        

    }

    return render(request,'transfer.html',context)

def livescore(request):
    current_date = datetime.now().strftime("%d %B")
    leagues = League.objects.prefetch_related('matches').all()
    context={
        'current_date': current_date,
        'leagues': leagues
        
    }
    return render(request, 'livescore.html', context)
def about(request):
    return render(request,'about.html')



def home_articlea(request):
    home_articles = Home_article_1.objects.all()
    Context={
        'home_articles':home_articles
    }


    return render(request, 'home-article-1.html',Context)
def home_articleb(request):
 
    home_articles = Home_article_2.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-2.html',Context)
def home_articlec(request):
    home_articles = Home_article_3.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-3.html',Context)
def home_articled(request):
    home_articles = Home_article_4.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-4.html',Context)
def home_articlee(request):
    home_articles = Home_article_5.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-5.html',Context)
def home_articlef(request):
    home_articles = Home_article_6.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-6.html',Context)
def home_articleg(request):
    home_articles = Home_article_7.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-7.html',Context)
def home_articleh(request):
    home_articles = Home_article_8.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-8.html',Context)
def home_articleg(request):
    home_articles = Home_article_9.objects.all()
    Context={
        'home_articles':home_articles
    }
    return render(request,'home-article-9.html',Context)
def newsa(request):
    news_articles = News_article_1.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-1.html',Context)
def newsb(request):
    news_articles = News_article_2.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-2.html',Context)
def newsc(request):
    news_articles = News_article_3.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-3.html',Context)
def newsd(request):
    news_articles = News_article_4.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-4.html',Context)
def newse(request):
    news_articles = News_article_5.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-5.html',Context)

def newsg(request):
    news_articles = News_article_6.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-6.html',Context)

def newsh(request):
    news_articles = News_article_7.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-7.html',Context)

def newsi(request):
    news_articles = News_article_8.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-8.html',Context)
def newsf(request):
    news_articles = News_article_9.objects.all()
    Context={
        'news_articles':news_articles
    }
    return render(request,'News-article/news-article-9.html',Context)
def tranfera(request):
    transfer_articles = Transfer_article_1.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-1.html',Context)

def tranferb(request):
    transfer_articles = Transfer_article_2.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-2.html',Context)

def tranferc(request):
    transfer_articles = Transfer_article_3.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-3.html',Context)

def tranferd(request):
    transfer_articles = Transfer_article_4.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-4.html',Context)

def tranfere(request):
    transfer_articles = Transfer_article_5.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-5.html',Context)

def tranferf(request):
    transfer_articles = Transfer_article_6.objects.all()
    Context={
        'transfer_articles':transfer_articles
    }
    return render(request, 'transfers-article/tranfer-article-6.html',Context)

def tranferg(request):
    return render(request, 'transfers-article/tranfer-article-7.html')

def tranferh(request):
    return render(request, 'transfers-article/tranfer-article-8.html')

def tranferi(request):
    return render(request, 'transfers-article/tranfer-article-9.html')