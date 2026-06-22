# inventory/serializers.py


from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    # We accept the author's name as a write-only string from the user
    author_name = serializers.CharField(write_only=True)
    # We output the actual author data as read-only
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author', 'author_name']

    def create(self, validated_data):
        """
        This custom create method handles the <<extend>> relationship : creating an author if they are missing.
        """
        author_name = validated_data.pop('author_name')
        
        # Get the existing author, or create a brand new one
        author_instance, created = Author.objects.get_or_create(name=author_name)
        
        # Create and return the book linked to this author
        book = Book.objects.create(author=author_instance, **validated_data)
        return book