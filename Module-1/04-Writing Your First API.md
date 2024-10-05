# Getting Started with Your First Django API Project

## Introduction

In this project, you will create a simple API for a bookstore to manage their book collection. You’ll be following CRUD principles—Create, Read, Update, and Delete—using standard API conventions, including HTTP methods and status codes.

---

### Project Overview

A bookstore requires a web and mobile application to streamline book management. The API will enable managers to quickly add and edit books, while visitors can browse the collection.

### Step 1: Create a Django Model

To store book information in the database, you need a Django model. This model will define how data is structured and stored.

**Book Model Fields**:

- **Title**: CharField with a max length of 255.
- **Author**: CharField with the same specifications as Title.
- **Price**: DecimalField with a maximum of five digits and two decimal places.
- **Inventory**: PositiveSmallIntegerField (optional) to indicate stock availability.

### Step 2: Set Up API Endpoints

You will create two API endpoints for the bookstore:

1. **`/api/books`**: This endpoint will return a list of all books in the database, including those out of stock.
2. **`/api/books/{book_id}`**: This endpoint will return details of a specific book. If the book does not exist, it should return a **404 Not Found** status code. For successful requests, it should return a **200 OK** status code.

**Response Format**:

- The response for a single book should not be enclosed in square brackets, as it is not part of an array.

### Step 3: Create a New Book

To create a new book, you will send an HTTP **POST** request to the `/api/books` endpoint.

- If successful, the API should return the newly created book with a **201 Created** status code.
- If required data is missing (e.g., the author's name), it should return an error message with a **400 Bad Request** status code.

### Step 4: Convert Model to JSON

API responses are typically delivered in JSON format. To convert a single model instance to a JSON response:

1. Import `model_to_dict` from `django.forms.models`.
2. Import `JsonResponse` from `django.http`.
3. Retrieve a book record by ID and convert it to a JSON object.

### Step 5: Editing and Deleting Books

To edit or delete a book, you will use HTTP **PUT** and **DELETE** requests respectively.

- For these operations, create a URL pattern: `/api/books/<int:pk>/`.

**Handling Requests**:

- Data is sent in the HTTP body as either raw JSON or form URL encoded.
- Use `QueryDict` from `django.http` to parse the request body into a Python dictionary, allowing you to access individual elements.

### Recap of Key Steps

1. Create a Django model to represent the books.
2. Set up API endpoints to handle requests for all books and specific books.
3. Convert model instances to JSON for API responses.
4. Implement create, edit, delete, and soft delete functionality.
5. Parse the HTTP body to access request data.

With careful planning and understanding of the required concepts, you can efficiently implement your API project with minimal debugging. Now that you have a solid foundation, writing the actual working code should be straightforward. Good luck with your project!

### Organizing Your Django API Project for Maintainability

#### Importance of Upfront Planning

Effective organization at the beginning of a project can save you significant time and effort later. By planning ahead, you ensure that your project remains maintainable, allowing for easier feature additions and bug fixes down the road.

---

### Key Strategies for Project Organization

1. **Split Large Apps into Multiple Apps**
   - Break down a large application into smaller, focused apps. Each app should address a specific set of related problems.
   - This modular approach enhances productivity and prevents the application from becoming unmanageable, avoiding frustrating delays and complex debugging.

2. **Use Virtual Environments**
   - Avoid using the global environment for project dependencies to prevent version conflicts.
   - Utilize a virtual environment (e.g., with `pipenv`) to isolate dependencies, ensuring that each project has only the packages it needs without conflicts.

3. **Implement API Versioning**
   - When upgrading an API, create a new version to keep the old one intact. This allows client developers time to adapt their applications to the new API.
   - Always create a separate app for the new version to facilitate management and avoid cluttering the original app.

4. **Maintain a `requirements.txt` File**
   - Keep a list of packages and their versions in a `requirements.txt` file to ensure consistency across deployments.
   - For `pip`, use the command `pip3 freeze > requirements.txt`. With `pipenv`, use the `Pipfile.lock` to track dependencies.

5. **Organize Resources by App**
   - Create separate resource folders for each app to avoid conflicts and streamline file management.
   - Store static files and templates specific to each app within their respective directories for better organization.

6. **Split Settings into Multiple Files**
   - Instead of a single, long settings file, divide settings into separate files and include them in the main settings module. This simplifies management and makes it easier to locate specific settings.
   - Explore Django's split settings functionality for implementation.

7. **Centralize Business Logic in Models**
   - Place relevant business logic within your models rather than in views. This practice keeps code organized, reusable, and easier to manage.

---

### Recap of Best Practices

- **Split your app into multiple, focused apps.**
- **Use a virtual environment to manage dependencies.**
- **Version your APIs for backward compatibility.**
- **List dependencies in a `requirements.txt` file.**
- **Organize resources with separate folders for each app.**
- **Split settings into multiple files for better manageability.**
- **Keep business logic in models for cleaner, reusable code.**

By following these organizational strategies, you enhance the maintainability and productivity of your Django API projects. This structure not only makes future updates easier but also leads to more efficient development practices overall. Well done on prioritizing organization in your project!
