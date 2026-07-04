from django.urls import path
from .views import BookInventoryView, BookDetailView, BulkBookInventoryView

urlpatterns = [
    # Your existing, working URLs
    path('api/books/inventory/', BookInventoryView.as_view(), name='book-inventory'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # NEW: Make sure this is added right below the others!
path('books/bulk/', BulkBookInventoryView.as_view(), name='book-bulk')]