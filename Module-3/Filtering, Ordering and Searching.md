# Implementing Search and Filtering in API for Little Lemon

## Overview

- Modern apps and websites commonly feature a search function.
- Enhancing the Little Lemon website/app requires adjusting API endpoints for effective searching and filtering.

### Importance of Filtering

- **Problem Statement**: Users may want to view specific items (e.g., appetizers, items within a price range, or items containing certain keywords).
- **Filtering**: Allows client applications to request a subset of results based on specific criteria.

### Two Approaches to Filtering

1. **Client-Side Filtering**:
   - API returns all records; filtering is managed by the client.
   - Pros: Easier to develop.
   - Cons: Inefficient for large datasets, causing server load.

2. **Server-Side Filtering**:
   - API processes filtering, returning only relevant records.
   - Pros: Reduces server load and simplifies client development.
   - Cons: Requires more initial development time.

### Implementation Steps

1. **Adapting API Endpoints**:
   - Focus on filtering menu items by category, name, and price.

2. **Constructing Filter Queries**:
   - Example of filter queries:
     - By category: `?category=main`
     - By price: `?to_price=3`
     - Combined: `?category=main&to_price=3`

3. **Modifying Views**:
   - In `views.py`, add parameters to the menu items function to handle filtering.
   - Retrieve query parameters:

     ```python
     category_name = request.query_params.get('category')
     price = request.query_params.get('to_price')
     ```

   - Use an `if` block to check for parameter values and filter items accordingly:
     - For category:

       ```python
       if category_name:
           items = items.filter(category__title=category_name)
       ```

     - For price:

       ```python
       if price:
           items = items.filter(price__lte=to_price)
       ```

4. **Field Lookups**:
   - Use `__` (double underscore) for field lookups:
     - Example for category: `category__title`
     - Example for price: `price__lte` (less than or equal)

5. **Testing the API**:
   - Visit the menu items endpoint with different filter values to see results.

### Implementing Search Functionality

- **Search by Name**:
  - Add a search parameter in the query string:
    - Example: `?search=chocolate`
  - Implement in the views:

    ```python
    search = request.query_params.get('search')
    if search:
        items = items.filter(name__startswith=search)
    ```

- **Different Search Options**:
  - To check if characters appear anywhere in the title: use `icontains`.
  - For case-insensitive starts with: use `istartswith`.

### Conclusion

- Optimizing API results with search and filtering enhances user experience.
- Understanding field lookups as comparison operators is crucial for effective querying.

## Implementing Ordering/Sorting in API for Little Lemon

- This video focuses on implementing ordering or sorting of API results based on query strings.
- The `django-filters` package offers advanced filtering, sorting, and searching but is typically used with class-based views. This guide will utilize Django's native sorting methods for function-based views.

- **Ordering**: Allows users to sort results in ascending or descending order based on specified fields.

### Implementing Sorting in API

1. **Adding Ordering Parameter**:
   - Modify the menu items endpoint to accept an `ordering` query string.
   - Example endpoint: `http://127.0.0.1:8000/api/menu-items?ordering=price`

2. **Modify Views**:
   - Open the menu items function and add the ordering parameter:

     ```python
     ordering = request.query_params.get('ordering')
     ```

   - Before serializing the items, sort the query set:

     ```python
     items = items.order_by(ordering)
     ```

3. **Testing Ascending Order**:
   - Visit the menu items endpoint with `ordering=price`.
   - Result: Items sorted in ascending order by price.

4. **Changing to Descending Order**:
   - To sort in descending order, append a minus sign to the field name:
   - Example: `ordering=-price`.
   - No code changes are needed; the endpoint will handle this automatically.

### Sorting by Multiple Fields

1. **Sorting by Two Fields**:
   - To sort by multiple fields, use a comma-separated query string:
   - Example: `ordering=price,inventory`.
   - This sorts items first by price and then by inventory in ascending order.

2. **Implementation for Multiple Fields**:
   - Split the `ordering` string:

     ```python
     ordering_fields = ordering.split(',')
     ```

   - Use the `order_by` method with the list:

     ```python
     items = items.order_by(*ordering_fields)
     ```

3. **Combining Ascending and Descending Orders**:
   - To sort by price (ascending) and inventory (descending):
   - Example: `ordering=price,-inventory`.
   - The minus sign before `inventory` indicates descending order.

- You have learned how to implement sorting in your API results using Django’s built-in `order_by` method.
- The ability to accept multiple fields in the query string allows for flexible sorting options.

### Data Validation in Django REST Framework (DRF)

#### Importance of Data Validation

- Ensures user-submitted data is valid, meets requirements, and is safe for the database.
- Critical for maintaining data integrity in web applications.

#### Key Concepts of Validation

- **Validation**: The process of checking that data is in the correct format and meets specified criteria.
- Common validation cases in the Little Lemon API include:
  - **Price**: Must be greater than 2.0.
  - **Stock**: Cannot be negative.
  - **Title**: Must be unique.

#### Validation Techniques in DRF

1. **Basic Validation Rules**
   - Ensure that price is not 0 or negative.
   - Prevent duplicate titles for menu items.

2. **Serializers in DRF**
   - Two main serializers in `serializers.py`:
     - `MenuItemSerializer`
     - `CategorySerializer`

#### Methods for Validation in `MenuItemSerializer`

1. **Method 1: Conditions in the Field**
   - Use `DecimalField` for price:

     ```python
     price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
     ```

   - This enforces that price must be at least 2.0.

2. **Method 2: Using `extra_kwargs` in the Meta Class**
   - Validate fields using `extra_kwargs`:

     ```python
     class Meta:
         model = MenuItem
         fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
         extra_kwargs = {
             'price': {'min_value': 2},
             'stock': {'source': 'inventory', 'min_value': 0}
         }
     ```

3. **Method 3: Using `validate_field()` Methods**
   - Define custom validation methods for each field:

     ```python
     def validate_price(self, value):
         if value < 2:
             raise serializers.ValidationError('Price should not be less than 2.0')
     
     def validate_stock(self, value):
         if value < 0:
             raise serializers.ValidationError('Stock cannot be negative')
     ```

4. **Method 4: Using the `validate()` Method**
   - Validate multiple fields simultaneously:

     ```python
     def validate(self, attrs):
         if attrs['price'] < 2:
             raise serializers.ValidationError('Price should not be less than 2.0')
         if attrs['inventory'] < 0:
             raise serializers.ValidationError('Stock cannot be negative')
         return super().validate(attrs)
     ```

#### Unique Validation

- **UniqueValidator**: Ensures the uniqueness of a single field.
  - Example for title:

    ```python
    extra_kwargs = {
        'title': {
            'validators': [UniqueValidator(queryset=MenuItem.objects.all())]
        }
    }
    ```

- **UniqueTogetherValidator**: Ensures the uniqueness of a combination of fields.
  - Example for title and price:

    ```python
    validators = [
        UniqueTogetherValidator(
            queryset=MenuItem.objects.all(),
            fields=['title', 'price']
        ),
    ]
    ```

- Data validation is essential for maintaining data integrity in DRF.
- Various methods can be employed to validate data within serializers, ensuring inputs meet the defined requirements.

# Data Sanitization Notes

## Introduction

- **Definition**: Sanitization cleans data from potential threats.
- **Risks**: Without sanitization, APIs can be vulnerable to SQL injection and client-side attacks like cross-site scripting and session hijacking.
- **Importance**: Data validation alone is insufficient; additional sanitization processes may be necessary.

## Sanitizing HTML and JavaScript

- **Need for Sanitization**: User input may contain malicious HTML tags (e.g., `<script>`, `<img>`), leading to harmful script execution.
- **Example**: Input like `Tomato Pasta <script>alert('hello')</script>` can execute unwanted scripts if not sanitized.
- **Tool**: Use the third-party package **Bleach** to sanitize input by converting HTML special characters into HTML entities.

### Installation Steps

1. **Install Bleach**:

   ```bash
   pipenv install bleach
   ```

2. **Import in serializers.py**:

   ```python
   import bleach
   ```

### Sanitization in Serializer

- **Validate Method**: Sanitize the title field in the `MenuItemSerializer`:

   ```python
   def validate_title(self, value):
       return bleach.clean(value)
   ```

- **Sanitize Multiple Fields**:

   ```python
   def validate(self, attrs):
       attrs['title'] = bleach.clean(attrs['title'])
       if attrs['price'] < 2:
           raise serializers.ValidationError('Price should not be less than 2.0')
       if attrs['inventory'] < 0:
           raise serializers.ValidationError('Stock cannot be negative')
       return super().validate(attrs)
   ```

### Testing

- **POST Request**: Send data with HTML tags; the sanitizer will convert tags into entities, ensuring safety.

## Preventing SQL Injection

- **Definition**: SQL injection involves attackers injecting SQL queries into input data to manipulate the database.
- **Prevention Strategy**: Avoid raw SQL unless absolutely necessary; when using raw SQL, escape parameters with string placeholders.

### Correct Usage

- **Parameterized Query** (Recommended):

   ```python
   limit = request.GET.get('limit')
   MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit])
   ```

### Incorrect Usages

- **String Formatting** (Vulnerable):

   ```python
   limit = request.GET.get('limit')
   MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s' % limit)
   ```

- **Quotation with Placeholder** (Vulnerable):

   ```python
   limit = request.GET.get('limit')
   MenuItem.objects.raw("SELECT * FROM LittleLemonAPI_menuitem LIMIT '%s'", [limit])
   ```

## Conclusion

- **Key Takeaway**: Data sanitization is crucial for protecting against threats like script injection and SQL injection.
- **Practical Knowledge**: You now understand methods to effectively sanitize data in Django Rest Framework (DRF).

## Pagination in API Notes

### Importance of Pagination

- **Definition**: Pagination breaks down large datasets into smaller, manageable chunks.
- **Example**: With 1000 orders in a database, fetching all orders at once can overload the server and waste bandwidth. Instead, serving only the latest 10 orders reduces load.
- **Client Control**: Clients can specify page numbers and the number of records per page, enhancing efficiency.

## Implementation Overview

1. **Request Example**:
   - To fetch the 7th and 8th menu items:

```bash
   GET /menu-items?per_page=2&page=4
```

- Page Breakdown:
  - Page 1: Records 1-2
  - Page 2: Records 3-4
  - Page 3: Records 5-6
  - Page 4: Records 7-8

2. **Limit Maximum Records**:
   - Set a maximum limit (e.g., 10 records per page) to prevent abuse.
   - If a client requests 20 records, they must make two calls:
     - First call: 10 records from page 3 (records 21-30).
     - Second call: 10 records from page 4 (records 31-40).
   - For excessive requests (e.g., 50 records), return a 400 Bad Request status.

## Implementing Pagination in Django REST Framework (DRF)

1. **Setup**:
   - Open `views.py` and modify the menu items function.
   - Accept query string parameters `per_page` and `page`.
   - Default values: `per_page = 2`, `page = 1`.

2. **Code Snippet**:

   ```python
   from django.core.paginator import Paginator, EmptyPage

   def menu_items(request):
       per_page = request.GET.get('per_page', 2)
       page = request.GET.get('page', 1)
       
       # Fetch items (assuming `items` is your queryset)
       paginator = Paginator(items, per_page)
       
       try:
           items = paginator.page(page)
       except EmptyPage:
           items = []  # Handle non-existing pages
   ```

3. **Testing**:
   - **No Query String**: Access the endpoint without parameters to see two items per page.
   - **With Query Strings**: Access the endpoint with `?per_page=3&page=1` to see three items.

## Conclusion

- **Key Takeaway**: Pagination is crucial for efficient API management, saving server resources and improving client experience.
- **Tools Used**: Implemented pagination using Django’s Paginator module and handled potential errors with try-except blocks.

## Filtering and Pagination in Django REST Framework (DRF) Notes

- **Overview**: Learn to implement filtering, searching, and pagination using built-in classes in DRF with class-based views.
- **Focus**: Utilize features to enhance API efficiency and usability.

## Project Scaffolding

### Step 1: Create Class-Based View

- Extend `ModelViewSet` for CRUD operations on menu items:

  ```python
  from rest_framework.response import Response
  from rest_framework import viewsets
  from .models import MenuItem
  from .serializers import MenuItemSerializer

  class MenuItemsViewSet(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
  ```

### Step 2: Update URLs

- Map the view to endpoints in `urls.py`:

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list'})),
      path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
  ]
  ```

### Step 3: Configure Settings

- Add filters in `settings.py`:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': [
          'rest_framework.renderers.JSONRenderer',
          'rest_framework.renderers.BrowsableAPIRenderer',
          'rest_framework_xml.renderers.XMLRenderer',
      ],
      'DEFAULT_FILTER_BACKENDS': [
          'django_filters.rest_framework.DjangoFilterBackend',
          'rest_framework.filters.OrderingFilter',
          'rest_framework.filters.SearchFilter',
      ],
  }
  ```

## Ordering and Sorting

- **Implement Sorting**: Enable sorting by price and inventory:

  ```python
  class MenuItemsViewSet(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
      ordering_fields = ['price', 'inventory']
  ```

- **Usage**: Access the API and use the filter button to sort results by the specified fields. You can also combine sorting:

  ```bash
  GET /api/menu-items?ordering=price,inventory
  ```

## Pagination

- **Enable Pagination**: Configure default pagination settings:

  ```python
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE': 2
  ```

- **Effect**: Only two records are displayed per page, with pagination controls in the browsable API interface.

## Search Functionality

- **Implement Search**: Allow searching by title:

  ```python
  class MenuItemsViewSet(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
      ordering_fields = ['price', 'inventory']
      search_fields = ['title']
  ```

- **Functionality**: Search results are case-insensitive due to the default lookup behavior (`icontains`).

## Searching Nested Fields

- **Search by Related Model**: Extend search to category titles:

  ```python
  class MenuItemsViewSet(viewsets.ModelViewSet):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer
      ordering_fields = ['price', 'inventory']
      search_fields = ['title', 'category__title']
  ```

- **Naming Convention**: Use `RelatedModelName_FieldName` (e.g., `category__title`) for nested searches.

## Conclusion

- **Key Takeaway**: Implementing filtering, pagination, and searching in DRF is straightforward with built-in classes, enhancing API efficiency and usability.

## Caching in API Infrastructure Notes

### Importance of Caching

- **Overview**: Caching serves pre-stored results instead of generating fresh ones for every request, reducing server load and bandwidth usage.
- **Scenario**: Increased traffic (e.g., after positive reviews) can overwhelm servers; caching helps mitigate this risk.

## HTTP Request Flow in Layered Architecture

1. **Request Flow**:
   - Visitor → Firewall → Reverse Proxy Server → Web Server → Database Server → Response Back
2. **Caching Layers**:
   - **Client**
   - **Reverse Proxy**
   - **Web Server**
   - **Database Server**

## Caching Mechanisms

### 1. Database Server Caching

- **Function**: Most modern databases implement caching to minimize read-write operations.
- **Method**: Typically uses a **query cache** to store SQL queries and their results in memory.
  - If no changes are detected, the cached result is served, saving processing time and resources.
- **Limitation**: Solely relying on database caching is inefficient, as server-side scripts still need to connect to the database for cached results.

### 2. Web Server Caching

- **Function**: Server-side scripts can cache responses if data hasn't changed since the last query.
- **Storage Options**:
  - Simple files
  - Database
  - Caching tools (e.g., Redis, Memcached)
- **Example**: If an application receives 1,000 hits per minute but updates data once a day, the server can cache the response and serve the same result multiple times without querying the database, significantly reducing load.

### 3. Reverse Proxy Caching

- **Function**: Distributes requests across multiple web servers, helping manage high traffic.
- **Mechanism**: Web servers send responses with caching headers; reverse proxies cache these responses for a specified time.
  - This prevents web servers from becoming overwhelmed with requests.

### 4. Client-Side Caching

- **Function**: Clients (browsers/applications) cache responses based on caching headers sent from the server.
- **Behavior**: During the caching period, the client decides whether to use the cached response or make a new server request.
- **Recommendation**: While client-side caching is helpful, it's crucial to implement proper caching strategies on the server side for consistency and reliability.

## Conclusion

- **Key Takeaway**: Properly implemented caching at various layers (client, reverse proxy, web server, and database) can significantly reduce resource consumption and improve performance.
- **Final Note**: Understanding and applying these caching techniques is essential for handling increased traffic effectively and maintaining a responsive application.
