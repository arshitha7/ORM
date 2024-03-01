# Ex02 Django ORM Web Application
## Date: 01-02-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<Screenshot 2024-03-01 093807.png>)
## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import book,bookAdmin
admin.site.register(book,bookAdmin)

models.py

from django.db import models
from django.contrib import admin
class book(models.Model):
   book_name=models.CharField(max_length=30)
   pages=models.IntegerField()
   author=models.CharField(max_length=20)
   price=models.IntegerField()
   release_date=models.DateField()

class bookAdmin(admin.ModelAdmin):
   list_display=('book_name','pages','author','price','release_date')


```

## OUTPUT

![alt text](<Screenshot 2024-03-01 091605.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
