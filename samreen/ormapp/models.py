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

