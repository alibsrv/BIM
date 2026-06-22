# Readers Haven API 📚

A robust, scalable Django REST Framework backend designed to automate inventory management for independent bookstores. 

## Project Overview
This API transitions the bookstore's inventory from a manual ledger to a normalized relational database. It features intelligent data serialization to prevent duplicate entries and a highly flexible, future-proof search engine.

## Core Features
* **Smart Data Entry:** Utilizing custom `get_or_create` serializer logic, the API automatically links existing authors or creates new profiles seamlessly during book creation.
* **Zero-Touch Dynamic Filtering:** Built with Python model introspection, the search endpoint automatically detects database columns, allowing users to filter by any attribute without hardcoded search logic.
* **Relational Spanning:** Supports complex URL queries (e.g., `?author=King`) to search across database tables using Django's double-underscore relationship lookups.
* **Automated Test Suite:** Comprehensive test coverage verifying creation logic, search functionality, and graceful empty-state handling.

## Tech Stack
* **Language:** Python
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite (Development)
* **Testing:** Django `APITestCase`

## API Endpoints

### 1. Add a Book to Inventory
* **URL:** `/api/books/add/`
* **Method:** `POST`
* **Payload Example:**
  ```json
  {
      "title": "The Shining",
      "price": "14.99",
      "author_name": "Stephen King"
  }