from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    # author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE) #many books to 1 author (order of tables matters) #need to add(on_delete=models.CASCADE) for django 2.0
    author = models.ManyToManyField(Author, related_name='books') #many to many (order doesnt matter) #dont need (on_delete) for many to many 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






