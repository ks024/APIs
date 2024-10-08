# Django Rest Framework (DRF) Setup and Configuration Notes

## Overview

Django Rest Framework (DRF) is a powerful toolkit for quickly building Web APIs in Django. This guide covers how to install, configure, and create an API endpoint with DRF using both `pip` and `pipenv`.

### Installation Options

- **Pip**:
  - Requires manual management of dependencies and virtual environments.
- **Pipenv**:
  - Simplifies dependency management and creates/handles virtual environments automatically.

### Steps to Set Up DRF with Pipenv

1. **Open Terminal** and navigate to your project directory.
2. **Install Django**:

   ```bash
   pipenv install django
   ```

3. **Activate the Virtual Environment**:

   ```bash
   pipenv shell
   ```

4. **Create a Django Project and App**:

   ```bash
   django-admin startproject BookList
   python manage.py startapp BookListAPI
   ```

5. **Install DRF**:

   ```bash
   pipenv install djangorestframework
   ```

### Configuration of DRF

1. **Modify `settings.py`**:
   - Locate the `INSTALLED_APPS` section and add:

     ```python
     'rest_framework',
     'BookListAPI',
     ```

2. **Create an API Endpoint**:
   - **View Definition**: Open `views.py` in `BookListAPI` and use the `@api_view` decorator to define the API view. Example:

     ```python
     from rest_framework.decorators import api_view
     from rest_framework.response import Response

     @api_view(['GET', 'POST'])
     def book_list(request):
         # Your logic for GET/POST requests
         return Response(data)
     ```

   - **URL Routing**: Create a `urls.py` file in `BookListAPI` and add your view:

     ```python
     from django.urls import path
     from .views import book_list

     urlpatterns = [
         path('books/', book_list),
     ]
     ```

3. **Include the App's URLs in the Main Project**:
   - In the main `urls.py` of the `BookList` directory, add:

     ```python
     from django.urls import include

     urlpatterns = [
         path('api/', include('BookListAPI.urls')),
     ]
     ```

### Testing the API Endpoint

1. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

2. **Access the API**:
   - For GET requests: Visit `http://127.0.0.1:8000/api/books`.
   - Use tools like Insomnia or Postman to test the endpoint.

3. **Handling Different HTTP Methods**:
   - If a POST request is made without defining it in the decorator, it will return a method not allowed error.
   - To enable POST, update the `@api_view` decorator to include it:

     ```python
     @api_view(['GET', 'POST'])
     ```
