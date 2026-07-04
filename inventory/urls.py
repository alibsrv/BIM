# inventory/urls.py
from django.urls import path
from .views import (
    BookInventoryView,
    AddBookView,
    BookDetailView,
    BulkBookInventoryView,
)

# NOTE: the project urls.py already includes this file under the "api/" prefix
# (path('api/', include('inventory.urls'))), so paths here must NOT repeat "api/".
urlpatterns = [
    # Week 1: add a single book (+ author)
    path('books/add/', AddBookView.as_view(), name='add-book'),

    # Week 1 + Week 3: list, search (?search=), filter (?author=), sort (?sort=)
    path('books/inventory/', BookInventoryView.as_view(), name='book-inventory'),

    # Week 4: bulk add / bulk delete
    path('books/bulk/', BulkBookInventoryView.as_view(), name='book-bulk'),

    # Week 2: retrieve / update / delete a single book by primary key
    # NOTE: keep this AFTER the literal paths above so "bulk" and "add"
    # are not swallowed by <int:book_id>.
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
]