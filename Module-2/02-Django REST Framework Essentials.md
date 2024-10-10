# Notes on Using Serializers in Django Rest Framework (DRF)

## Overview

Data conversion is crucial in API development, and serializers in DRF simplify this process. They help convert Django models into readable formats like JSON or XML, and vice versa.

## Functions of Serializers

1. **Data Representation**: Pull data from the database using Django models and present it to clients.
2. **Data Conversion**: Convert user-supplied data into models for safe storage in the database.
3. **Data Integrity**: Validate and ensure the integrity of data before storage, preventing corruption.
4. **Serialization and Deserialization**:
   - **Serialization**: Convert complex data types (like Django models) into readable formats.
   - **Deserialization**: Parse JSON data and map it to existing models while validating the data.

## Practical Implementation

### 1. Create a Serializer File

Create a file named `serializers.py` in your Django app directory to house all serializer-related code.

### 2. Define the Model

Example model in `models.py`:

```python
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
```

### 3. Fetch All Menu Items

In `views.py`, create a method to retrieve all menu items:

```python
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def menu_items(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)
```

### 4. Implement the Serializer

In `serializers.py`, define the serializer:

```python
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['price']  # Specify fields to display
        # Optionally exclude fields: exclude = ['title', 'inventory']
```

### 5. Test the Menu Items Endpoint

Visit the menu items endpoint to see the JSON data representation. Sensitive fields can be omitted from the serializer to protect them.

## Handling Single Records

### 1. Create a Method for Single Item Retrieval

Add a method in `views.py`:

```python
@api_view(['GET'])
def menu_item_detail(request, id):
    try:
        item = MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
```

### 2. Update `urls.py`

Map the single item method in your URLs:

```python
from django.urls import path
from .views import menu_items, menu_item_detail

urlpatterns = [
    path('menu-items/', menu_items),
    path('menu-items/<int:id>/', menu_item_detail),
]
```

### 3. Test the Single Item Endpoint

Ensure you have existing records before testing the endpoint. Implement error handling for non-existing IDs to return a friendly JSON error message.

## Conclusion

Serializers in DRF streamline the process of converting database records to JSON and vice versa, saving development time. Upcoming lessons will cover how to enhance serializers further using model serializers for even more efficient data handling.

## Notes on Using Model Serializers in Django Rest Framework (DRF)

- Model serializers in DRF simplify the process of converting Django model instances to JSON, requiring less code than standard serializers.

### Key Concepts

1. **ModelSerializer**: A special type of serializer that automatically creates fields based on the model, allowing for quicker serialization of model instances.
2. **Field Customization**:
   - You can easily change the name of a field in the output (e.g., changing `inventory` to `stock`) using the `source` argument.
   - You can also add calculated fields to the serializer.

### Practical Implementations

1. **Define the Model**
   - Example model in `models.py`:

     ```python
     class MenuItem(models.Model):
         title = models.CharField(max_length=100)
         price = models.DecimalField(max_digits=10, decimal_places=2)
         inventory = models.IntegerField()
     ```

2. **Create the Model Serializer**
   - Open or create `serializers.py` in your Django app and define the serializer:

     ```python
     from rest_framework import serializers
     from .models import MenuItem

     class MenuItemSerializer(serializers.ModelSerializer):
         stock = serializers.IntegerField(source='inventory')  # Renaming field

         price_after_tax = serializers.DecimalField(
             source='price',  # Link to existing field
             read_only=True
         )

         class Meta:
             model = MenuItem
             fields = ['title', 'price', 'stock', 'price_after_tax']  # Include new field
     ```

3. **Adding a Calculated Field**
   - To add a field for `price_after_tax`, define a method in the serializer:

     ```python
     from decimal import Decimal

     class MenuItemSerializer(serializers.ModelSerializer):
         stock = serializers.IntegerField(source='inventory')
         price_after_tax = serializers.DecimalField(read_only=True)

         class Meta:
             model = MenuItem
             fields = ['title', 'price', 'stock', 'price_after_tax']

         def get_price_after_tax(self, obj):
             return round(obj.price * Decimal('1.10'), 2)  # Calculate price with tax
     ```

4. **Testing the Endpoints**
   - Visit the menu items endpoint and the single item endpoint to verify that the new serializer works without requiring changes in `views.py`.

## Notes on Using Relationship Serializers in Django Rest Framework (DRF)

- In Django projects, related data often spans multiple tables. To effectively manage these relationships, DRF provides relationship serializers that help convert related models to JSON for display.

### Key Concept

1. **Establishing Relationships**:
   - Use ForeignKey to connect models (e.g., `MenuItem` and `Category`).
   - Protect the integrity of relationships using `on_delete=models.PROTECT`, preventing the deletion of categories with associated menu items.

2. **Creating the Category Model**:
   - Define a new `Category` model in `models.py` and connect it to the `MenuItem` model.
   - Ensure to create migrations and migrate the database.

3. **Basic Serializer Implementation**:
   - Initially, add the `category` field to the `MenuItemSerializer` to include the category ID in the JSON output.
   - However, if you want to display the category name instead, further steps are needed.

### Implementing Relationship Serializers

1. **Modify the Category Model**:
   - Implement a `__str__` method in the `Category` model to specify how it should be represented as a string (e.g., displaying the category name).

   ```python
   class Category(models.Model):
       name = models.CharField(max_length=100)

       def __str__(self):
           return self.name
   ```

2. **Update the Views**:
   - Optimize the view to load related models in a single SQL query. This reduces the number of queries executed, improving efficiency.

   ```python
   from django.shortcuts import get_object_or_404
   from .models import MenuItem
   from rest_framework.decorators import api_view
   from rest_framework.response import Response

   @api_view(['GET'])
   def menu_items(request):
       items = MenuItem.objects.select_related('category').all()  # Use select_related for efficiency
       serializer = MenuItemSerializer(items, many=True)
       return Response(serializer.data)
   ```

3. **Creating a Category Serializer**:
   - In `serializers.py`, create a new `CategorySerializer`:

   ```python
   from rest_framework import serializers
   from .models import Category

   class CategorySerializer(serializers.ModelSerializer):
       class Meta:
           model = Category
           fields = ['id', 'name']  # Include relevant fields
   ```

4. **Integrate the Category Serializer**:
   - Modify the `MenuItemSerializer` to use the `CategorySerializer` for the category field:

   ```python
   class MenuItemSerializer(serializers.ModelSerializer):
       category = CategorySerializer()  # Use the CategorySerializer for the category field

       class Meta:
           model = MenuItem
           fields = ['title', 'price', 'inventory', 'category']  # Include the nested category
   ```

5. **Testing the Menu Items Endpoint**:
   - Visit the menu items endpoint to confirm that the category field now displays the category name with each menu item.

## Types of Serializers in Django Rest Framework (DRF)

In DRF, serializers are essential for converting complex data types, like querysets and model instances, into native Python data types. This note covers different serialization techniques, including nested fields and displaying related model fields as hyperlinks.

## 1. Nested Fields

### Method 1: Using a Category Serializer

To display related model fields (e.g., Category) as nested fields in the API output:

```python
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
```

### Method 2: Using the Depth Option

Alternatively, you can use the `depth` option in the `Meta` class to automatically include nested fields without creating separate serializers:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
        depth = 1  # Automatically include related fields

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
```

### Benefits of Nested Fields

Using nested fields provides more context and reduces the need for multiple API calls, making client applications simpler.

## 2. Displaying Related Model Fields as Hyperlinks

### Method 1: Using HyperlinkedRelatedField

#### Step 1: Create a View for the Related Model

Define a view that handles requests for the related model (e.g., Category):

```python
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
```

#### Step 2: Map the View in URLs

Add a URL pattern for the category detail view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:pk>', views.category_detail, name='category-detail'),
]
```

#### Step 3: Use HyperlinkedRelatedField in the Serializer

Modify the MenuItemSerializer to use `HyperlinkedRelatedField` for the category field:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='category-detail'
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
```

#### Step 4: Add Context to the Serializer

When serializing items, ensure you pass the request context:

```python
serialized_item = MenuItemSerializer(items, many=True, context={'request': request})
```

### Method 2: Using HyperlinkedModelSerializer

For a more streamlined approach, you can extend the `HyperlinkedModelSerializer` instead of `ModelSerializer`:

```python
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
```

### URL Patterns for HyperlinkedModelSerializer

Make sure to include the relevant URL patterns:

```python
urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    path('category/<int:pk>', views.category_detail, name='category-detail'),
]
```

In this note, you learned how to use the depth option for nested model fields and how to display related fields as hyperlinks using `HyperlinkedRelatedField` and `HyperlinkedModelSerializer`. These techniques enhance the API's usability and reduce the need for additional API calls.

## Note on Deserialization in Django Rest Framework (DRF)

Deserialization is the process of converting incoming request data into a format that can be saved as a model instance in DRF. This note covers how to implement deserialization, validate data, and manage read-only fields for API endpoints.

## Steps for Deserialization and Validation

### 1. Enable POST Method Support

- In your views file (`views.py`), modify the menu items function to support both GET and POST requests. Use the `@api_view` decorator:

```python
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        # Retrieve records
        pass
    elif request.method == 'POST':
        # Create a new record
        pass
```

### 2. Deserializing Request Data

- To deserialize incoming data, pass the request data to the serializer. Check for essential fields and validate the data:

```python
from .serializers import MenuItemSerializer

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        # Retrieve records
        pass
    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new record
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

### 3. Validating Data

- Use the `is_valid()` method to validate incoming data. If the data is valid, access it via `validated_data`:

```python
if serializer.is_valid():
    validated_data = serializer.validated_data
    serializer.save()  # Save the new record
```

### 4. Handling Required Fields

- If required fields are missing (e.g., category), the serializer will raise an error. For example, you can mark the category field as read-only in the serializer to prevent it from being required during POST requests:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Make category read-only

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category']  # No category_id yet
```

### 5. Adding a Category ID Field

- If you want to allow saving a menu item with a specific category ID, add `category_id` to the serializer:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)  # Make category_id write-only

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category', 'category_id']
```

### 6. Hiding Fields in GET Requests

- If you want to hide the `category_id` field in GET requests while keeping it available for POST, use the `write_only=True` argument:

```python
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)  # Only for POST

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category']  # Do not include category_id
```

### 7. Submitting POST Requests

- After making the above changes, you can submit a POST request with a JSON payload to create a new menu item. Ensure the required fields are included in the request body.

In this guide, you learned how to implement deserialization in DRF to convert HTTP request data into model instances, validate that data, and save it to the database. You also explored how to manage read-only fields to control data exposure based on request types. By using different serializers for GET and POST requests, you can streamline your API's functionality and enhance data integrity.

## Renderers in Django Rest Framework (DRF)

Renderers in DRF are responsible for formatting the API output to various data types, making your API more flexible and usable across different client applications. This note covers how to configure and use different renderers, including JSON, XML, and YAML.

## Types of Renderers

DRF supports several built-in and third-party renderers:

1. **JSON Renderer**: The default renderer that outputs data in JSON format.
2. **Browsable API Renderer**: Provides a web interface for interacting with the API (only available with `Accept: text/html`).
3. **XML Renderer**: A third-party renderer for XML output.
4. **YAML Renderer**: A third-party renderer for YAML output.
5. **JSONP Renderer**: A third-party renderer for JSONP output.

## Configuring Renderers

### 1. Setting Up Renderers

To configure the renderers used by your API, you can modify the `settings.py` file of your Django project. If you want to use specific renderers, define them in the `REST_FRAMEWORK` setting:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',  # Commented out to disable browsable API
    )
}
```

### 2. Testing API Output

To test the output of your API with different renderers:

- **JSON Output**: By default, DRF responds with JSON unless specified otherwise.
- **Browsable API**: To enable the browsable interface, ensure the `Accept` header is set to `text/html`. When accessed via a web browser, this header is sent automatically.

#### Example in Insomnia

1. **Send a JSON request**: By default, without specifying the `Accept` header, you will receive JSON.
2. **Send a Browsable API request**: Set the `Accept` header to `text/html` and observe the change to the browsable interface.

### 3. Adding XML Support

To add XML support, install the `djangorestframework-xml` package:

```bash
pipenv install djangorestframework-xml
```

Then, update your `settings.py` to include the XML renderer:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework_xml.renderers.XMLRenderer',  # Add this line for XML support
    )
}
```

### 4. Testing XML Output

To test the XML renderer:

1. Set the `Accept` header in Insomnia to `application/xml`.
2. Send a request to the API endpoint (e.g., `/api/menu-items`).
3. The response will now be in XML format.

### 5. Summary of Renderer Behavior

- **Default Behavior**: Without an `Accept` header, DRF uses the JSON renderer.
- **Browsability**: Requires `Accept: text/html`.
- **XML Support**: Add the XML renderer and set `Accept: application/xml` to receive XML output.

Renderers in DRF are essential for displaying API responses in various formats, enhancing the API's usability across different clients. By configuring the appropriate renderers in your settings, you can control the output format and provide a more flexible API experience. You learned how to use JSON, XML, and the browsable API renderer effectively, making your API adaptable to different client needs.

## Different Types of Renderers in Django Rest Framework (DRF)

Renderers in DRF are essential for formatting API output in various formats, such as JSON, XML, and more. This note covers several renderers available in DRF, including the **TemplateHTMLRenderer**, **StaticHTMLRenderer**, **CSVRenderer**, and **YAMLRenderer**. Each renderer has unique use cases and can enhance the usability of your API.

---

## TemplateHTMLRenderer

The `TemplateHTMLRenderer` allows you to render HTML responses, making it useful for applications that require well-formatted outputs, such as invoicing systems. This renderer leverages Django’s templating language to create dynamic HTML content.

### Steps to Implement TemplateHTMLRenderer

#### Step 1: Import Required Classes

In your `views.py` file, import `TemplateHTMLRenderer` and the `renderer_classes` decorator:

```python
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
```

#### Step 2: Create the Menu Function

Define a new function that utilizes the `TemplateHTMLRenderer` to return menu items as HTML:

```python
@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data': serialized_item.data}, template_name='menu-items.html')
```

#### Step 3: Create the HTML Template

Create the HTML template `menu-items.html` inside the `templates` directory of your Django app:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Menu Items</title>
</head>
<body>
    <table width="100%" style="text-align: left;">
        <tr>
            <th>Item</th>
            <th>Price</th>
            <th>Price After Tax</th>
            <th>Stock</th>
        </tr>
        {% for item in data %}
        <tr>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.price_after_tax }}</td>
            <td>{{ item.stock }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

#### Step 4: Map the Function to an Endpoint

Update your `urls.py` file to create a new endpoint for the menu:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    path('menu', views.menu),  # New endpoint for the HTML output
]
```

Now, when you access the endpoint at `http://127.0.0.1:8000/api/menu`, it will display all menu items in a neatly formatted HTML table.

---

## StaticHTMLRenderer

The `StaticHTMLRenderer` is used to display static HTML content without needing Django's templating language.

### Steps to Implement StaticHTMLRenderer

#### Step 1: Import Required Classes needed

In your `views.py` file, import `StaticHTMLRenderer` and the `renderer_classes` decorator:

```python
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
```

#### Step 2: Create the Welcome Function

Define a function that returns a static HTML message:

```python
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)
```

#### Step 3: Map the Function to an Endpoint

Update your `urls.py` file to add the new endpoint:

```python
path('welcome', views.welcome)
```

Now, visiting `http://127.0.0.1:8000/api/welcome` will display a welcome message in HTML format.

---

## CSV Renderer

CSV (Comma-Separated Values) is a popular format for displaying data, especially in tabular forms.

### Steps to Implement CSV Renderer

#### Step 1: Install CSV Renderer

Install the third-party CSV renderer package:

```bash
pipenv install djangorestframework-csv
```

#### Step 2: Import the CSV Renderer

In your `views.py`, import the CSV renderer:

```python
from rest_framework_csv.renderers import CSVRenderer
```

#### Step 3: Use the CSV Renderer

Add the `CSVRenderer` to the `renderer_classes` decorator in your menu-items function:

```python
@api_view()
@renderer_classes([CSVRenderer])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)
```

Now, when you access the endpoint at `http://127.0.0.1:8000/api/menu-items`, you will receive the output in CSV format.

---

## YAML Renderer

YAML is another popular data format used for API responses, offering a more human-readable structure than JSON.

### Steps to Implement YAML Renderer

#### Step 1: Install YAML Renderer

Install the YAML renderer package:

```bash
pipenv install djangorestframework-yaml
```

#### Step 2: Import the YAML Renderer

In your `views.py`, import the YAML renderer:

```python
from rest_framework_yaml.renderers import YAMLRenderer
```

#### Step 3: Use the YAML Renderer

Add the `YAMLRenderer` to the `renderer_classes` decorator in your menu-items function:

```python
@api_view()
@renderer_classes([YAMLRenderer])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)
```

Now, when you access the endpoint at `http://127.0.0.1:8000/api/menu-items`, you will receive the output in YAML format.

---

## Global Settings for Renderers

Instead of importing the CSV and YAML renderers individually in each view, you can make them available globally in your API project. This allows clients to receive the desired output by sending the appropriate `Accept` header.

### Steps to Set Global Renderers

1. Open `settings.py`.
2. Add the following lines in the `DEFAULT_RENDERER_CLASSES` section:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
    ]
}
```

Now clients can specify the response format using the following headers:

- **CSV**: `Accept: text/csv`
- **YAML**: `Accept: application/yaml`

---

In this note, you learned how to use various renderers in your DRF-based API project to display output in different formats, including HTML, CSV, and YAML. These renderers enhance the flexibility and usability of your API, catering to diverse client needs. For more detailed information on available renderers, refer to the DRF documentation.

---

## Week 2 Review: Django Rest Framework (DRF)

Congratulations on completing the second week of the course! Here’s a summary of what you’ve learned about using DRF to create APIs, serialize database models, and manage data.

## Introduction to DRF

- **What is DRF?**: A toolkit built on top of Django for efficient API creation, allowing data retrieval, processing, and representation in formats like JSON and XML.
- **Key Benefits**:
  - Built-in API viewer for easy inspection.
  - Human-readable HTTP status codes.
  - Built-in serializers for data conversion and deserialization.

## Installation and Configuration

- **Pipenv vs. Pip**:
  - Pipenv manages virtual environments and dependencies automatically, simplifying package management compared to pip.

## API View Decorators

- **API Decorators**: Facilitate rapid prototyping, inspection, and testing of APIs directly in the browser.

## Routers in DRF

- **Auto-configuration**: Routers automatically set up URLs for class-based views, reducing the need for individual URL patterns.

## Function vs. Class-Based Views

- **Creating Views**: Learned to create both function and class-based views.
- **Advantages of Class-Based Views**:
  - Less code duplication.
  - Extensibility.
  - Specific methods for different HTTP requests.

## Debugging with Django Debug Toolbar

- **SQL Section**: An essential tool for monitoring SQL queries and optimizing performance.

## Restaurant Menu API Project

- **API Functionality**: Created a menu API capable of creating, listing, editing, deleting, and selecting menu items.
- **Book List API Conversion**: Applied learned skills to convert a book list project to DRF.

## DRF Essentials

- **Serializers**:
  - Practical demonstrations on how to use serializers to manage data.
  - Relationship serializers for displaying related model data.

## Deserialization Techniques

- **Validation and Mapping**: Techniques to validate HTTP request bodies and map them to existing models for database storage.

## Renderers in DRF

- **Types of Renderers**: Responsible for displaying API output in various formats (JSON, XML, HTML).
- **Third-Party Renderers**: Options available beyond built-in renderers.

## Ungraded Lab

- **Restaurant Menu API**:
  - Worked on serialization, validation, and deserialization.
  - Displayed API data in JSON and XML, and created HTML forms for menu item management.

## Skills Acquired

By the end of this week, you should be able to:

- Install and set up DRF.
- Create API endpoints using function and class-based views.
- Serialize database models using model serializers.
- Validate and convert data with serialization.
- Map user input to data models with deserialization.
- Utilize throttling and caching to optimize and protect your API.

## Additional Resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this section.

- [XML renderer, XML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-xml/)
- [YAML renderer, YAML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-yaml/)
- [JSONP renderer, JSONP support for Django REST framework](https://jpadilla.github.io/django-rest-framework-jsonp/)
