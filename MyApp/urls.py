from django.urls import path
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('',views.home, name='home'),
    path('books/<int:id>', views.book, name="books"),
    path('books', views.books, name="allbooks"),
    path('register', views.register.as_view(), name="registration"),
    path('search/', views.search, name='search'),
    path('searched/', views.searchwords, name='searchwords'),
    path("user/", views.profile, name="profile"),
    path('', auth_login, name="login"),
]
