from django.urls import path, include
from django.views.generic import RedirectView
from . import views
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('registration.backends.default.urls')),
    # path('accounts/', include('registration.auth_urls')),
    # path('profile', RedirectView.as_view(url="favorite.html", permanent=True)),
    # path('favorite/', views.user_favorite_view, name="favorite"),
    path('books/<slug:slug>/', views.book_detail_view, name="book-detail"),
    path('category/<slug:slug>', views.category_detail_view, name="category-detail"),
]
