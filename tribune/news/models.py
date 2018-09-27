from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def save_editor(self):
        self.save()

    def __str__(self):
        return self.first_name
        

    class meta:
        ordering = ['first_name'] 

class tags(models.Model):
    name = models.CharField(max_length = 30)

    # def save_tags(self):
    #     self.save()


    def __str__(self):
        return self.name          


class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')
    
    # class method that takes in an object an return data for today article
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
        
    # class method that takes in an object and return a data according to a given date 
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date_date = date)
        return news



    def __str__(self):
        return self.title


    def save_article(self):
        self.save()

   
