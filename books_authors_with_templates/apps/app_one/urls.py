from django.urls import path 
from . import views #remember to import views 

urlpatterns = [
    path('', views.book), #this is the basic [Localhost8000] page
    path('process', views.process_book), #the rediect page to store and print data from database
    path('books/<id>', views.book_info), # id you have a passing parameter remember to pass in views function 
    path('authors', views.author),
    path('processa', views.process_author), #the rediect page to store and print data from database
    path('authors/<id>', views.author_info),
    ]
