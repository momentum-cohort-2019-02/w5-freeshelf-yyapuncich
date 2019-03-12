from django.contrib import admin
from core.models import Book, Author, Catagory

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'url')

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
