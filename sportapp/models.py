from django.db import models


# Create your models here.
#Showcase 
class Homepage(models.Model):
    
    
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)

#articles
class Homepage1(models.Model):
    
    
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)

#homepage models
class Homepage2(models.Model):
    
    
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)


class Homepage3 (models.Model):
    
    
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
#newspage models
class Newspage1(models.Model):
    
    
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)

class Newspage2(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
class Newspage3(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
class Newspage4(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
  #transferpage  sections model  
class Transfepage1(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100) 
class Transfepage2(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
class Transfepage3(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)  
class Transfepage4(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    urls=models.CharField(max_length=100)
class Livescore(models.Model):
    img=models.ImageField(upload_to='pic')
    head=models.CharField(max_length=100)
    time = models.TimeField()  
    match= models.CharField(max_length=100)

 # Leagues  in livescore Model
class League(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name  

# matches in each league model
class Match(models.Model):
    league = models.ForeignKey(League, related_name='matches', on_delete=models.CASCADE)
    time = models.TimeField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.time}"

# Home articles models
class Home_article_1(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph(models.Model):
    home_article_1 = models.ForeignKey(Home_article_1, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.home_article_1.head}"    
    
class Home_article_2(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph2(models.Model):
    home_article_2 = models.ForeignKey(Home_article_2, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.home_article_2.head}"    


class Home_article_3(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph3(models.Model):
    home_article_3 = models.ForeignKey(Home_article_3, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.home_article_3.head}"    



class Home_article_4(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph4(models.Model):
    home_article_4 = models.ForeignKey(Home_article_4, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.home_article_4.head}"    


class Home_article_5(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph5(models.Model):
    Home_article_5 = models.ForeignKey(Home_article_5, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Home_article_5.head}" 


class Home_article_6(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph6(models.Model):
    Home_article_6 = models.ForeignKey(Home_article_6, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Home_article_6.head}" 
    

class Home_article_7(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph7(models.Model):
    Home_article_7 = models.ForeignKey(Home_article_7, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Home_article_7.head}" 


class Home_article_8(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph8(models.Model):
    Home_article_8 = models.ForeignKey(Home_article_8, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Home_article_8.head}"
    


class Home_article_9(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph9(models.Model):
    Home_article_9 = models.ForeignKey(Home_article_9, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Home_article_9.head}"
    
# News articles models
class News_article_1(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1a(models.Model):
    News_article_1 = models.ForeignKey(News_article_1, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_1.head}"


class News_article_2(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1b(models.Model):
    News_article_2 = models.ForeignKey(News_article_2, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_2.head}" 
    


class News_article_3(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1c(models.Model):
    News_article_3 = models.ForeignKey(News_article_3, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_3.head}"


class News_article_4(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1d(models.Model):
    News_article_4 = models.ForeignKey(News_article_4, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_4.head}"



class News_article_5(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1e(models.Model):
    News_article_5 = models.ForeignKey(News_article_5, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_5.head}" 


class News_article_6(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1f(models.Model):
    News_article_6 = models.ForeignKey(News_article_6, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_6.head}"




class News_article_7(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1g(models.Model):
    News_article_7 = models.ForeignKey(News_article_7, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_7.head}"


class News_article_8(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1h(models.Model):
    News_article_8 = models.ForeignKey(News_article_8, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_8.head}"



class News_article_9(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph1i(models.Model):
    News_article_9 = models.ForeignKey(News_article_9, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.News_article_9.head}"  

# Transfer articles models
class Transfer_article_1(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph11(models.Model):
    Transfer_article_1 = models.ForeignKey(Transfer_article_1, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_1.head}" 


class Transfer_article_2(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph12(models.Model):
    Transfer_article_2 = models.ForeignKey(Transfer_article_2, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_2.head}"
    

class Transfer_article_3(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph13(models.Model):
    Transfer_article_3 = models.ForeignKey(Transfer_article_3, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_3.head}"



class Transfer_article_4(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph14(models.Model):
    Transfer_article_4 = models.ForeignKey(Transfer_article_4, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_4.head}" 



class Transfer_article_5(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph15(models.Model):
    Transfer_article_5 = models.ForeignKey(Transfer_article_5, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_5.head}"
    

class Transfer_article_6(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph16(models.Model):
    Transfer_article_6 = models.ForeignKey(Transfer_article_6, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_6.head}"  


class Transfer_article_7(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph17(models.Model):
    Transfer_article_7 = models.ForeignKey(Transfer_article_7, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_7.head}" 


class Transfer_article_8(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph18(models.Model):
    Transfer_article_8 = models.ForeignKey(Transfer_article_8, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_8.head}" 



class Transfer_article_9(models.Model):
    head = models.CharField(max_length=100)
    p1 = models.CharField(max_length=1000)
    p2 = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.head

class Paragraph19(models.Model):
    Transfer_article_9 = models.ForeignKey(Transfer_article_9, related_name='paragraphs', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Paragraph for {self.Transfer_article_9.head}"          



