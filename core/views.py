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

    # Paginate here
    
    # Define context here
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'books': books,
    }
    # Render HTML template index.html with data in context
    return render(request, 'index.html', context=context)

def book_detail_view(request, slug):
    books = get_object_or_404(Book, slug=slug)
    slug = books.slug
    return render(request, "book-detail.html", {
        "books":books,
        "slug":slug,
        })

def category_detail_view(request):
    category = get_object_or_404(Category)
    return render(request, "category_detail.html", {"category": category})
