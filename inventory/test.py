from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookstoreTests(APITestCase):
    
    # 1. THE SETUP
    def setUp(self):
        # This creates a temporary, fake database just for testing
        self.author = Author.objects.create(name="Stephen King")
        self.book = Book.objects.create(title="The Shining", price="14.99", author=self.author)

    # 2. TEST: ADDING A BOOK
    def test_add_new_book_with_new_author(self):
        # We pretend to be the librarian adding a completely new book and author
        url = '/api/books/add/' 
        data = {
            "title": "Murder on the Orient Express",
            "price": "12.50",
            "author_name": "Agatha Christie"
        }
        
        response = self.client.post(url, data)
        
        # Check if it was successful (201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the new author was actually saved to the database
        self.assertEqual(Author.objects.count(), 2)

    # 3. TEST: SEARCHING FOR A BOOK
    def test_search_by_existing_author(self):
        # We pretend to search for "King"
        url = '/api/books/inventory/?author=King'
        response = self.client.get(url)
        
        # Check if the search worked (200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if it found exactly 1 book
        self.assertEqual(len(response.data), 1)
        # Check if the book it found is The Shining
        self.assertEqual(response.data[0]['title'], "The Shining")

    # 4. TEST: SEARCHING FOR A MISSING BOOK
    def test_search_author_not_found(self):
        # We pretend to search for an author that does not exist
        url = '/api/books/inventory/?author=J.K. Rowling'
        response = self.client.get(url)
        
        # Check if the system stayed online without crashing (200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the list returned is completely empty (0 results)
        self.assertEqual(len(response.data), 0)