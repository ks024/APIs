# Different Types of Routing in Django REST Framework (DRF)

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
