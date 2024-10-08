# Generic Views and ViewSets in DRF

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
