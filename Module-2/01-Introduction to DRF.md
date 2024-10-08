# Django Rest Framework (DRF)

## Overview

- Django is a powerful framework for developing web applications, but its API development capabilities can be enhanced with the Django Rest Framework (DRF).
- DRF is a toolkit built on top of Django that simplifies and speeds up the process of building robust APIs.

### Key Benefits of Using DRF

1. **Integration with Existing Django Apps**
   - Easily integrate DRF into your existing Django application with minimal configuration changes.

2. **API Viewer**
   - DRF includes an API viewer that allows developers to send HTTP requests and evaluate responses without needing external tools like Insomnia. While limited, it’s useful for quick experiments.

3. **Request and Response Objects**
   - DRF provides specialized request and response objects that offer enhanced flexibility for processing data compared to standard Django HTTP objects.

4. **Human-Readable HTTP Status Codes**
   - The `status` module in DRF offers human-readable representations of HTTP status codes, making your code more understandable. For example, use `status.HTTP_200_OK` instead of numeric codes like `200` or `404`.

5. **Built-in View Set Classes**
   - DRF's view sets simplify the creation of functional CRUD (Create, Read, Update, Delete) operations. They provide full support for necessary HTTP methods out of the box and can be extended for more complex workflows.

6. **Built-in Serializers**
   - DRF includes serializers that facilitate the conversion between complex data types (like database models) and native Python data types. This conversion allows easy rendering into formats such as JSON or XML.
   - Serializers also support deserialization, which validates and connects input data back to existing models, preventing data corruption.

7. **Authentication Support**
   - DRF simplifies the implementation of authentication systems, allowing for easy development of custom authentication layers.
   - It supports social authentication, enabling users to authenticate via external providers (e.g., Facebook).

### Conclusion

- DRF enhances the capabilities of Django for API development, making it faster and more efficient. This framework supports modern practices in serialization, request handling, and authentication, helping developers focus on building their applications.

## Django Rest Framework (DRF) Setup and Configuration Notes

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

## Benefits of Using the API View Decorator in Django Rest Framework (DRF)

The API View Decorator is a powerful feature in Django Rest Framework (DRF) that enhances the functionality and usability of API endpoints. This note outlines its key benefits and how to implement it in your DRF applications.

## Implementing the API View Decorator

1. **Importing Necessary Classes**:
   - To use the API View Decorator, import it from the `rest_framework.decorators` module:

     ```python
     from rest_framework.decorators import api_view
     ```

   - Also, import the `Response` class from the `rest_framework.response` module:

     ```python
     from rest_framework.response import Response
     ```

2. **Using the Decorator**:
   - Add the `@api_view` decorator above your view function:

     ```python
     @api_view(['GET', 'POST'])
     def books(request):
         # Your logic here
         return Response(data)
     ```

### Key Benefits of the API View Decorator

1. **Browsable API Interface**:
   - The API View Decorator transforms standard API output into a user-friendly browsable interface. This allows developers to easily test endpoints and view responses directly in the browser.
   - When using the `Response` class, the API output is polished, making it more readable.

2. **HTTP Method Support**:
   - You can specify which HTTP methods are supported by your function by passing them as an array to the `@api_view` decorator.
   - For example, adding `['GET', 'POST']` allows both GET and POST requests, and the browsable interface will show the allowed methods.

3. **Built-in Testing Features**:
   - The browsable API provides features like:
     - **Options Button**: Displays information about the current endpoint, including accepted content types and allowed methods.
     - **JSON Response**: Allows you to view responses in JSON format directly in the browser.

4. **In-browser JSON Input**:
   - With support for POST methods, you can submit JSON objects directly from the browser, eliminating the need for external tools like Postman or Insomnia.

5. **Throttling and Rate Limiting**:
   - The API View Decorator allows you to implement throttling, enabling you to limit how many times users can access the API in a specified period. More on this will be covered later in the course.

6. **Authentication**:
   - You can use the API View Decorator to authenticate endpoints, ensuring that only authenticated users can access specific API functions.

## Different Types of Routing in Django REST Framework (DRF)

**Introduction**  
Django REST Framework (DRF) offers various techniques for URL mapping or routing in an API project, simplifying the development process. This note outlines both traditional and advanced routing methods available in DRF.

---

## 1. Regular Routes

You can map functions from `views.py` to API endpoints using the `path` function from `django.urls`.

**Example**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
]
```

This maps the `books` function to the `/api/books` endpoint. You can specify HTTP methods using the `@api_view` decorator.

---

### 2. Routing to Class Methods

To map a specific method from a class, declare it as a `@staticmethod`.

**Example**:

```python
class Orders:
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)
```

**URLs**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.Orders.listOrders)
]
```

---

### 3. Routing Class-Based Views

When using a class that extends `APIView`, you can map it directly in `urls.py`.

**Example**:

```python
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message": "single book with id " + str(pk)}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)
```

**URLs**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:pk>', views.BookView.as_view())
]
```

This allows HTTP GET and PUT calls to the `/api/books/{bookId}` endpoint.

---

### 4. Routing Classes that Extend ViewSets

You can define classes extending different types of ViewSets for handling various HTTP requests.

**Example**:

```python
class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "All books"}, status=status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Creating a book"}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": "Updating a book"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status=status.HTTP_200_OK)
```

**URLs**:

```python
urlpatterns = [
    path('books', views.BookView.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>', views.BookView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }))
]
```

---

### 5. Routing with SimpleRouter

Using `SimpleRouter` allows automatic URL mapping for ViewSet classes without specifying individual methods.

**Example**:

```python
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

Access the endpoints `/api/books` and `/api/books/1` without manually mapping methods.

---

### 6. Routing with DefaultRouter

`DefaultRouter` provides the same functionality as `SimpleRouter` but includes an API root view that lists all endpoints.

**Example**:

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

Additionally, you can access the API root at `http://127.0.0.1:8000/api/`.

## Generic Views and ViewSets in DRF

Django REST Framework (DRF) provides various generic views and ViewSets to streamline API development, reducing boilerplate code and speeding up the process of building fully functional CRUD APIs.

## ViewSets

- **Definition**: ViewSets are class-based views that simplify the creation of APIs by encapsulating the logic for different HTTP methods.
- **Benefits**: Automatically generates browsable APIs and allows for easy permission and throttle management.

### Key ViewSet Classes

1. **ViewSet**:
   - Base class for defining standard actions.
   - Requires manual database operation coding.
   - Common methods:
     - `retrieve()`: GET (Display a single resource)
     - `update()`: PUT (Replace a single resource)
     - `partial_update()`: PATCH (Partially update a resource)
     - `destroy()`: DELETE (Delete a resource)

   ```python
   class MenuItemViewSet(viewsets.ViewSet):
       # Define methods here
   ```

2. **ModelViewSet**:
   - Automatically handles CRUD operations.
   - Requires only a queryset and serializer.

   ```python
   class MenuItemView(viewsets.ModelViewSet):
       queryset = MenuItem.objects.all()
       serializer_class = MenuItemSerializer
   ```

3. **ReadOnlyModelViewSet**:
   - For read-only endpoints (only supports GET requests).

   ```python
   class ReadOnlyMenuItemView(viewsets.ReadOnlyModelViewSet):
       queryset = MenuItem.objects.all()
       serializer_class = MenuItemSerializer
   ```

### Generic Views

- **Definition**: Generic views offer specific functionalities to create APIs without needing to write all the underlying logic manually.
- **Usage**: Requires importing from `rest_framework.generics`.

#### Key Generic Views

1. **CreateAPIView**: Handles POST requests for creating a new resource.
2. **ListAPIView**: Handles GET requests for displaying a collection of resources.
3. **RetrieveAPIView**: Handles GET requests for displaying a single resource.
4. **DestroyAPIView**: Handles DELETE requests for deleting a resource.
5. **UpdateAPIView**: Handles PUT and PATCH requests for updating resources.
6. **ListCreateAPIView**: Combines listing and creating functionalities.
7. **RetrieveUpdateAPIView**: Combines retrieving and updating functionalities.
8. **RetrieveDestroyAPIView**: Combines retrieving and deleting functionalities.
9. **RetrieveUpdateDestroyAPIView**: Combines all operations for a single resource.

```python
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```

### Authentication

- **Global Authentication**: Set `permission_classes` for the entire class.
  
  ```python
  permission_classes = [IsAuthenticated]
  ```

- **Selective Authentication**: Override `get_permissions` to selectively require authentication based on the HTTP method.

```python
def get_permissions(self):
    permission_classes = []
    if self.request.method != 'GET':
        permission_classes = [IsAuthenticated]
    return [permission() for permission in permission_classes]
```

### Returning Items for Authenticated Users Only

- Override `get_queryset` to filter resources based on the authenticated user.

```python
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
```

### Overriding Default Behavior

- Override default methods (like `get`, `post`, etc.) to customize behavior.

```python
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  

    def get(self, request, *args, **kwargs):
        return Response('new response')
```

## Class-Based Views in Django REST Framework (DRF)

Class-based views (CBVs) in DRF allow for cleaner and more organized code compared to function-based views (FBVs). Each approach has its own advantages: FBVs are simpler and easier to read, while CBVs reduce code duplication and facilitate code reuse through inheritance.

## Key Benefits of Class-Based Views

- **Less Code**: CBVs minimize boilerplate code, allowing for quicker implementation.
- **Organization**: Group related functionalities within a single class, improving code structure.
- **Method-Specific Handling**: Each HTTP method (GET, POST, etc.) can have its own dedicated method, making the code easier to manage.

### Implementing Class-Based Views

1. **Creating a Class-Based View**:
   - Import `APIView` and `Response` from DRF.
   - Extend the `APIView` class to create a new view (e.g., `BookList`).
   - Define methods like `get` and `post` that correspond to HTTP verbs.

   ```python
   from rest_framework.views import APIView
   from rest_framework.response import Response

   class BookList(APIView):
       def get(self, request):
           # Logic for GET
           return Response({"message": "List of books"})

       def post(self, request):
           # Logic for POST
           return Response({"message": "Book created"})
   ```

2. **Mapping the View to URLs**:
   - In `urls.py`, map the class to an endpoint without needing to map each method individually.

   ```python
   from django.urls import path
   from .views import BookList

   urlpatterns = [
       path('api/books', BookList.as_view()),
   ]
   ```

3. **Handling Query Parameters**:
   - Use `request.GET.get('parameter')` to access query string parameters.
   - Example: Filter books by author using `/api/books?author=Hemingway`.

4. **Handling Payloads in POST Requests**:
   - Use `request.data.get('key')` to retrieve data from the request body (JSON or form-encoded).
   - Example: Return the title from the JSON payload sent in a POST request.

5. **Creating a View for Single Resources**:
   - Create another class (e.g., `Book`) for operations on individual books.
   - Include a primary key (pk) in methods like `get`, `put`, and `delete`.

   ```python
   class Book(APIView):
       def get(self, request, pk):
           # Logic for retrieving a single book
           return Response({"message": "Book details"})

       def put(self, request, pk):
           # Logic for updating a single book
           return Response({"message": "Book updated"})
   ```

6. **Mapping the Single Resource View**:
   - Update `urls.py` to map the new class to an endpoint that includes the primary key.

   ```python
   urlpatterns += [
       path('api/books/<int:pk>', Book.as_view()),
   ]
   ```

### Additional Features

- **Throttling and Authentication**: CBVs support throttling and authentication out of the box, enhancing security and performance.

Class-based views in DRF streamline API development by reducing code redundancy and enhancing organization. By leveraging HTTP method-specific methods and built-in features, developers can create clean and efficient APIs.

## Integrating Django Debug Toolbar

The Django Debug Toolbar is an essential tool for Django developers, helping to debug and optimize projects effectively. It provides insights into project settings, requests, database queries, and more.

## Installation Steps

1. **Install the Toolbar**:
   - Open your terminal and activate your virtual environment with:

     ```bash
     pipenv shell
     ```

   - Install the Django Debug Toolbar:

     ```bash
     pipenv install django-debug-toolbar
     ```

2. **Update `settings.py`**:
   - Add `'debug_toolbar'` to the `INSTALLED_APPS` section:

     ```python
     INSTALLED_APPS = [
         # other apps,
         'debug_toolbar',
     ]
     ```

3. **Add Middleware**:
   - Include the debug toolbar middleware in the `MIDDLEWARE` section:

     ```python
     MIDDLEWARE = [
         # other middleware,
         'debug_toolbar.middleware.DebugToolbarMiddleware',
     ]
     ```

4. **Configure Internal IPs**:
   - Create an `INTERNAL_IPS` section in `settings.py`:

     ```python
     INTERNAL_IPS = [
         '127.0.0.1',
     ]
     ```

### Using the Debug Toolbar

- **Accessing the Toolbar**:
  - Visit any endpoint, e.g., `/api/books`. The toolbar should appear on the right side of the screen.

- **Toolbar Features**:
  - **Settings**: Displays project settings and allows you to override them directly.
  - **Headers**: Shows request and response header information.
  - **SQL Queries**: Lists all SQL queries executed for the current request, useful for performance tuning.
  - **Static Files**: Displays static files loaded for the current request.
  - **Cache**: Shows applications using caching mechanisms.
  - **Profiling**: Offers a complete call stack, showing the execution flow of requests.

#### Important Notes

- The toolbar is only visible in development mode, not in production.
- You can hide or toggle sections of the toolbar for a cleaner view.

The Django Debug Toolbar is a powerful tool that aids in debugging and optimizing your Django API projects. By following the steps above, you can integrate it into your project and leverage its features for better performance and insights.
