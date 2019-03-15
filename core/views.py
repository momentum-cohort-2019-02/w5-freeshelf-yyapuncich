from django.shortcuts import render, get_object_or_404
from core.models import Book, Author, Category, Favorite
from django.core import paginator

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
    return render(request, "book-detail.html", {
        "books": books,
        })

def category_detail_view(request, slug):
    """View function for Categorie page to sort books by category"""
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter()
    return render(request, "category-detail.html", {
        "category": category,
        "books": books,
        })
