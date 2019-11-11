from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from MyApp.models import Book
# Create your views here.
def home(request):
    book_id=Book.objects.all()
    temp=loader.get_template('MyApp/test.html')
    dirr={"book_id":book_id}
    return HttpResponse(temp.render(dirr, request))
def book(request, id):
    booker=get_object_or_404(Book, pk=id)
    b={'book':booker}
    temp=loader.get_template('MyApp/subpage.html')
    return HttpResponse(temp.render(b, request))
