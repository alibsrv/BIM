# inventory/urls.py

from django.urls import path
from .views import AddBookView, BookInventoryView, BookDetailView

urlpatterns = [
    # A dedicated endpoint for viewing the full list
    path('books/inventory/', BookInventoryView.as_view(), name='book_inventory'),
    
    # A dedicated endpoint for adding new data
    path('books/add/', AddBookView.as_view(), name='add_book'),

    # A dedicated endpoint for modifying (PATCH/PUT) and deleting (DELETE) a specific book
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
]