from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookInventoryView(APIView):
    def get(self, request):
        books = Book.objects.all()
        
        # 1. Standard dynamic filter for direct Book fields (title, price, etc.)
        valid_fields = [f.name for f in Book._meta.get_fields() if not f.is_relation]
        filters = {}
        
        for key, value in request.query_params.items():
            if key in valid_fields:
                if isinstance(Book._meta.get_field(key), models.CharField):
                    filters[f"{key}__icontains"] = value
                else:
                    filters[key] = value
                    
        # 2. Add the relational filter for Author attributes
        # We check if the librarian typed '?author=...' in the URL
        author_search = request.query_params.get('author')
        if author_search:
            # The double underscore tells Django: 
            # Go to the 'author' ForeignKey, look at the 'name' field, and check if it contains the search word.
            filters['author__name__icontains'] = author_search
            
        # 3. Apply all filters (both regular and relational) at the same time
        books = books.filter(**filters)
        
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