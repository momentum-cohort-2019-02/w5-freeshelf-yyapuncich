from django.shortcuts import render, get_object_or_404, redirect
from core.models import Book, Author, Category, User
from django.core import paginator
from django.contrib.auth.decorators import login_required
from random import choice

# Create your views here.

def index(request):
    """View function for index of site."""
    # Generate counts of some main objects here
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    books = Book.objects.all()
    categories = Category.objects.all()

    # Paginate here
    
    # Define context here
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'books': books,
        'categories': categories,
    }
    # Render HTML template index.html with data in context
    return render(request, 'index.html', context=context)

def book_detail_view(request, slug):
    """Book detail page to show info for specific ebook"""
    books = get_object_or_404(Book, slug=slug)
    categories = Category.objects.all()
    return render(request, "book-detail.html", {
        "books": books,
        "categories": categories,
        })

def category_detail_view(request, slug):
    """View function for Categorie page to sort books by category"""
    category = get_object_or_404(Category, slug=slug)
    # Used a Field lookup on my books to get only books in the category on that page
    # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#field-lookups
    books = Book.objects.filter(categories__exact=category)
    return render(request, "category-detail.html", {
        "category": category,
        "books": books,
        })

@login_required
def user_favorite_view(request):
    """View for user favorites page"""
    books = Book.objects.all()
    user = User
    return render(request, 'favorite.html', {
        "books": books,
        "user": user,
    })


# Tried to use redirect in function like
# https://docs.djangoproject.com/en/2.1/topics/http/shortcuts/#redirect
# def profile_redirect_view(request):
#     """View for redirecting accounts/profile to favorite view"""
#     # profile_urls = ['/favorite/', '/profile/']
#     profile_url = ['/profile/']
#     return redirect(to='favorite.html', permanent=True)
