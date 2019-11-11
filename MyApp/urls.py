from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('books/<int:id>', views.book, name="books"),
]
