from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from django.db import models
from django.conf import settings

# Create your models here.
class User(AbstractUser):
   # name=models.CharField(max_length=200, default='')
    userImg = models.ImageField(upload_to='user_avas/', default='NULL')
    #surname=models.CharField(max_length=200, default='')
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=6, default='')
    info=models.TextField(default='')
    def __str__(self):
        return self.username
class Book(models.Model):
    reader=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=200, default='')
    rating=models.FloatField(default=0.0)
    text=models.TextField(default='')
    book_img = models.ImageField(upload_to='ImagesOfBooks/', default='NULL')
    def __str__(self):
        return self.name+" "+self.author
class Comment(models.Model):
    commentor=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    comment=models.TextField()
    def __str_(self):
        return self.book+" "+self.comment+"/n"
'''class User(AbstractUser):
    userImg = models.ImageField(upload_to='user_avas/', default='NULL')

    def __str__(self):
        return self.username'''
