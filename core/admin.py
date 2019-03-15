from django.contrib import admin
from core.models import Book, Author, Category, Favorite

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'book_url', 'slug')
    exclude = ('slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
