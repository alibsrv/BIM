# Readers Haven Inventory Management REST API

## Project Overview
This project is a Django-based REST API designed for independent bookstores to transition from manual ledgers to an automated digital system. It manages:
- Book inventory tracking
- Dynamic relational author profiling
- Advanced, automated search filtering

The API is implemented with a highly scalable architecture using Django REST Framework, featuring custom serialization logic to prevent duplicate database entries and "Zero-Touch" dynamic filters for future-proof searching.

## Technical Stack
- **Backend Framework:** Django & Django REST Framework (DRF)
- **Database:** SQLite (Development)
- **Architecture Pattern:** Function/Class-based Django views with JSON responses
- **Testing:** Django `APITestCase`

## UML Alignment (Relational Architecture)
The implementation follows a normalized relational database model to ensure data integrity:
- `Author` exists as an independent entity.
- `Book` is the dependent entity.
- **One-to-Many Relationship:** One `Author` can write multiple `Books`. The system automatically spans this relationship during queries, ensuring that updating an author's name once cascades perfectly across their entire library of books.

## Downloading from GitHub
To get a copy of this project on your local machine, you will first need to clone the repository using Git.

1. **Clone the repository:**
   Open your terminal and run the following command to download the code:
   ```bash
   git clone [https://github.com/alibsrv/BIM.git](https://github.com/alibsrv/BIM.git)
