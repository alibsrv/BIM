# Readers Haven Inventory Management System

## Project Overview
This project is an API-driven digital inventory management system built for "Readers Haven." It transitions a manual bookkeeping process into a scalable, highly efficient Django REST API. Developed as part of the Programming Clinic at Lancaster University Leipzig.

### Key Features
* **Full CRUD Operations:** Create, Read, Update, and Delete individual book and author records.
* **Dynamic Search & Filtering:** Case-insensitive search capabilities and advanced sorting (alphabetical, price ascending/descending) using `__icontains` and Django's `order_by`.
* **High-Efficiency Bulk Operations:** Dedicated batch processing endpoints utilizing `bulk_create` and `id__in` SQL transactions to safely handle massive data payloads without system lag during bi-annual grand sales.

## Technologies Used
* Python 3.10+
* Django 5.0.6
* Django REST Framework 3.15.1
* SQLite / PostgreSQL

## Setup & Installation

**1. Clone the repository**
```bash
git clone <https://github.com/alibsrv/BIM>
cd readers_haven_project


## Key Features
* **Full CRUD Operations:** Create, Read, Update, and Delete individual book and author records.
* **Dynamic Search & Filtering:** 
    * **Search:** Supports partial name matching (e.g., search for "Dune" using just "Du"). Uses case-insensitive matching (`__icontains`) for a user-friendly experience.
    * **Sorting:** Supports ascending and descending price/title sorting using query parameters.
* **High-Efficiency Bulk Operations:** Dedicated batch processing endpoints utilizing `bulk_create` to handle large data payloads during grand sales.

## API Usage Guide
You can test the search and sorting features directly in your browser or Postman by appending query parameters to the inventory URL: `http://127.0.0.1:8000/api/books/inventory/`

### 1. Search Functionality
Use the `search` parameter to filter books by title. The search is case-insensitive and partial-match capable.
* **Example:** `http://127.0.0.1:8000/api/books/inventory/?search=Dune`
* **Example (Partial):** `http://127.0.0.1:8000/api/books/inventory/?search=Du`

### 2. Sorting Functionality
Use the `sort` parameter to reorder the inventory.
* **Price Ascending:** `http://127.0.0.1:8000/api/books/inventory/?sort=price`
* **Price Descending:** `http://127.0.0.1:8000/api/books/inventory/?sort=-price`
* **Title Alphabetical:** `http://127.0.0.1:8000/api/books/inventory/?sort=title`
* **Title Reverse Alphabetical:** `http://127.0.0.1:8000/api/books/inventory/?sort=-title`

### 3. Combining Parameters
You can combine search and sorting to refine your view further.
* **Example:** `http://127.0.0.1:8000/api/books/inventory/?search=Foundation&sort=-price`