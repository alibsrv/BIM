from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookInventoryView(APIView):
    def get(self, request):
        # Start with the full list of books
        books = Book.objects.all()
        
        # --- 1. WEEK 6: SEARCH FUNCTIONALITY ---
        # Look for '?search=' in the URL
        search_query = request.query_params.get('search')
        if search_query:
            # __icontains makes it case-insensitive and matches partial or full titles
            books = books.filter(title__icontains=search_query)

        # --- 2. EXISTING WEEK 1 AUTHOR FILTER (Retained) ---
        author_search = request.query_params.get('author')
        if author_search:
            books = books.filter(author__name__icontains=author_search)

        # --- 3. WEEK 6: SORTING FUNCTIONALITY ---
        # Look for '?sort=' in the URL
        sort_query = request.query_params.get('sort')
        if sort_query:
            # Define allowed sorting options to prevent database errors
            valid_sorts = ['price', '-price', 'title', '-title']
            if sort_query in valid_sorts:
                # Rearrange the dataset based on the requested criteria
                books = books.order_by(sort_query)

        # Serialize and return the final data
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# --- CLASS 2:  FOR ADDING BOOKS ---
class AddBookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success! Book and Author saved.", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {"error": "Invalid Data", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
# --- CLASS 3: FOR READING, MODIFYING, AND DELETING A SPECIFIC BOOK ---
class BookDetailView(APIView):
    
    # Helper method to find the book or return None
    def get_object(self, book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    # NEW: Handle GET requests to view a single book
    def get(self, request, book_id):
        book = self.get_object(book_id)
        if not book:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, book_id):
        book = self.get_object(book_id)
        if not book:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # partial=True allows updating specific fields (like just the price)
        serializer = BookSerializer(book, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Book updated successfully",
                "book": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response({
            "error": "Invalid Data", 
            "details": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        book = self.get_object(book_id)
        if not book:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)