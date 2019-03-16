from django.contrib import admin
from core.models import Book, Author, Category

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'book_url')
    exclude = ('slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'books') 
    # Fix display here, books shows up funny on Admin site

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
