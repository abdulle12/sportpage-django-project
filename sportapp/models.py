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
  #transferpage model  
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
class League(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name  

class Match(models.Model):
    league = models.ForeignKey(League, related_name='matches', on_delete=models.CASCADE)
    time = models.TimeField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.time}"


    
    
    

     

   
