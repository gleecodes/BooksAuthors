from django.shortcuts import render, HttpResponse, redirect  #always remember to import what you need 
from .models import * # * means all 

# Book.objects.all().delete() #used to delete database if needed 
# Author.objects.all().delete()
def book(request): # request is always passed as parameter
    # return HttpResponse("is it working?") #to check id route is working
    books=Book.objects.all() #books is equal to all books in database
    print(books) #check to see if its printing info in terminal 
    context = {
        "books": books  #need this dictionary to list key and values to referance in HTML 
    }
    return render(request, "app_one/books_index.html", context) #context refers to dictionanry 

def process_book(request): #rerouting function to take info from form and rediect it back to first route 
    print(request.POST) #check if info is passing ...check terminal 
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('/')

def book_info(request,id): #remeber to put id as parameter 
    # print("this route is working")
    print(id)
    book = Book.objects.get(id=id) #remember you are trying to call one specific book 
    print(book) 
    context = { #need to be able to reference after it prints in termnial 
        "book" : book
        
    }   
    return render(request, "app_one/books_info.html", context)

def author(request):
    authors=Author.objects.all()
    print(authors)
    context = {
        "authors": authors
    }
    return render(request, "app_one/authors_index.html", context)

def process_author(request): # redirect for authors
    print(request.POST) #check if info is passing ...check terminal 
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors') #need slash in redirects 
    # return HttpResponse("route checking ")

def author_info(request,id):
    print(id)
    author = Author.objects.get(id=id) #remember you are trying to call one specific book 
    print(author) 
    context = { #need to be able to reference after it prints in termnial 
        "author" : author
    } 
    return render(request, "app_one/authors_info.html", context)
