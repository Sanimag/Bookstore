from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
# Create your views here.
def home(request):
    book_id=Book.objects.all().order_by('-rating')[:10]
    temp=loader.get_template('MyApp/index.html')
    dirr={"book_id":book_id}
    return HttpResponse(temp.render(dirr, request))
def book(request, id):
    booker=get_object_or_404(Book, pk=id)
    b={'book':booker}
    temp=loader.get_template('MyApp/subpage.html')
    return HttpResponse(temp.render(b, request))
def books(request):
    books=Book.objects.all()
    return render(request, 'MyApp/Books.html', {'book':books})
    
class register(CreateView):
    form_class = USERForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
def profile(request):
    try:
        books=Book.objects.all()
        return render(request, "MyApp/Profile.html", {'books':books, "empty":"There is no such book"})
    except:
        return render(request, "MyApp/Profile.html", {"empty":"There is no such book"})
def searchwords(request):
    try:
        if request.method=="POST":
            words = request.POST.get("search_field")
            if len(words)>0:
                result = Book.objects.filter(text__contains=words)
            return render(request, "MyApp/searchwords.html", {"result":result,"empty":"There is no such book"})
    except:
        return render(request, "MyApp/searchwords.html", {"empty":"There is no such book"})
def search(request):
    return render(request, "MyApp/search.html")
