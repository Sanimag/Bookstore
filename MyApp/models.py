from django.db import models

# Create your models here.
class Reader(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=6)
    def __str__(self):
        return self.name+" "+self.surname
class Book(models.Model):
    reader=models.ForeignKey(Reader, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    def __str__(self):
        return self.name+" "+self.author
class Comment(models.Model):
    commentor=models.ForeignKey(Reader, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    comment=models.TextField()
    def __str_(self):
        return self.book+" "+self.comment+"/n"
    
        
