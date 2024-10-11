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

### Summary

- You have learned how to implement sorting in your API results using Django’s built-in `order_by` method.
- The ability to accept multiple fields in the query string allows for flexible sorting options.

### Notes on Data Validation in Django REST Framework (DRF)

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

#### Conclusion
- Data validation is essential for maintaining data integrity in DRF.
- Various methods can be employed to validate data within serializers, ensuring inputs meet the defined requirements.