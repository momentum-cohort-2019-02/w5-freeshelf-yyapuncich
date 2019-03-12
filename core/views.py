from django.shortcuts import render
from core.models import Book, Author, Catagory

# Create your views here.

def index(request):
    """View function for index of site."""

    # Generate counts of some main objects here

    # Define context here
    context = {

    }
    # Render HTML template index.html with data in context
    return render(request, 'index.html', context=context)
    