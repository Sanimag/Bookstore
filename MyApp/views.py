from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('''<h3>For this time our bookstore have only these books(It will be better in the future):</h3>
<center/><b>1. Hamlet by William Shakespeare</b></center>
                            <center/><b>2. War and Peace by Leo Tolstoy </b></center>
                            <center/><b>3. Moby Dick by Herman Melville</b></center>
                            <center/><b>4. Don Quixote by Miguel de Cervantes</b></center>
                            <center/><b>5. Biography of Abram Lincoln by Jorg Kluni</b></center>
''')
