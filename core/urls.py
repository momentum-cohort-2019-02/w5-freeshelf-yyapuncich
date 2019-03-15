from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('registration.backends.default.urls')),
    path('books/<slug:slug>/', views.book_detail_view, name="book-detail"),
    path('category/<slug:slug>', views.category_detail_view, name="category-detail")
]
