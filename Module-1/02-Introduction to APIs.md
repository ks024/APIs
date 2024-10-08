# HTTP and HTTPS Overview

- **HTTP (Hypertext Transfer Protocol)**: Widely used for data transmission over the Internet.
- **HTTPS**: Secured version of HTTP that encrypts data for secure transmission, making it ideal for sensitive information like credit card details.

## Communication Process

1. **Client and Server**:
   - The client requests information.
   - The server responds with the requested content.

2. **Data Encryption (HTTPS)**:
   - Client encrypts data before sending it.
   - Server decrypts, processes the request, encrypts the response, and sends it back to the client, which decrypts it.

## Common HTTP Methods (Verbs)

| Method | Description                                  |
|--------|----------------------------------------------|
| GET    | Retrieves a resource                         |
| POST   | Sends data to create a record               |
| PUT    | Updates the entire resource                  |
| PATCH  | Partially updates a resource                 |
| DELETE | Deletes a resource                           |

### HTTP Requests

- Components include:
  - HTTP version (e.g., 1.1, 2.0)
  - URL/path
  - HTTP method
  - Request headers (e.g., cookies, user agents)
  - Optional body (e.g., raw JSON or form data)

### HTTP Responses

- Contains:
  - The requested resource
  - Content length and type
  - Response headers (e.g., cookies, ETags)
  - **HTTP Status Codes**: Indicate the result of the request.

### HTTP Status Codes

| Code Range | Meaning                        | Example                 |
|------------|--------------------------------|-------------------------|
| 200-299    | Successful responses           | 200 OK, 201 Created     |
| 300-399    | Redirection information        | 301 Moved Permanently   |
| 400-499    | Client errors                  | 404 Not Found           |
| 500-599    | Server errors                  | 500 Internal Server Error|

### Key Points

- Status codes provide information to the browser rather than the user.
- The same status code can have different meanings based on the context (e.g., 200 OK can mean different things for GET, PUT, or DELETE requests).
- Understanding these fundamental concepts is essential for developing sustainable and manageable APIs.

### HTTP Methods, Status Codes, and Response Types in REST APIs

#### Introduction

- Adhering to HTTP conventions is crucial for reducing bugs and facilitating easier API use by other developers.

## HTTP Methods

| Method | Description                                  | Example Endpoint                |
|--------|----------------------------------------------|----------------------------------|
| GET    | Retrieves a resource                         | `/api/menu-items`               |
| POST   | Sends data to create a record               | `/api/menu-items`               |
| PUT    | Replaces a resource entirely with the provided data | `/api/menu-items/1`          |
| PATCH  | Partially updates a resource                 | `/api/menu-items/1`             |
| DELETE | Removes a resource                           | `/api/menu-items/1`             |

### Example Endpoints for HTTP Methods

#### 1. **GET**

- **Endpoint**: `/api/menu-items`
  - **Description**: Retrieves a list of all menu items.
  - **Query Parameters**:
    - `?category=appetizers`: Filters items by category.
    - `?perpage=3&page=2`: Implements pagination, requesting 3 items on page 2.
  
- **Endpoint**: `/api/menu-items/1`
  - **Description**: Retrieves details for the specific menu item with ID 1.

#### 2. **POST**

- **Endpoint**: `/api/menu-items`
  - **Description**: Creates a new menu item.
  - **Sample JSON Payload**:

    ```json
    {
      "title": "Beef Steak",
      "price": 5.50,
      "category": "main"
    }
    ```

#### 3. **PUT**

- **Endpoint**: `/api/menu-items/1`
  - **Description**: Completely replaces the menu item with ID 1.
  - **Sample JSON Payload**:

    ```json
    {
      "title": "Chicken Steak",
      "price": 2.50,
      "category": "main"
    }
    ```

#### 4. **PATCH**

- **Endpoint**: `/api/menu-items/1`
  - **Description**: Partially updates the menu item with ID 1.
  - **Sample JSON Payload**:

    ```json
    {
      "price": 3.00
    }
    ```

  - **Note**: This will update only the price, leaving other attributes unchanged.

#### 5. **DELETE**

- **Endpoint**: `/api/menu-items/1`
  - **Description**: Deletes the menu item with ID 1.
  
- **Endpoint**: `/api/menu-items`
  - **Description**: Deletes all menu items in the collection. This action should be used with caution.

## Response Types

Common response formats include JSON, XML, plain text, and YAML.

| Format        | Example Header                    |
|---------------|-----------------------------------|
| JSON          | `Accept: application/json`        |
| XML           | `Accept: application/xml`         |
| HTML          | `Accept: text/html`               |
| YAML          | `Accept: application/yaml`        |

### Overview of REST APIs

#### What is REST?

- **REST (Representational State Transfer)**: An architectural style for designing APIs that is popular for its simplicity and ease of implementation. REST APIs facilitate communication between clients and servers to access and modify data.

#### Key Constraints of REST APIs

1. **Client-Server Architecture**: Separation between the client (consumer of resources) and server (provider of resources).
  
2. **Statelessness**: The server does not store client state. Each request from the client must contain all information needed to understand and process it, meaning the server doesn't remember previous interactions.

3. **Cacheable**: Responses can be cached to reduce server load and improve efficiency.

4. **Layered System**: The architecture can be divided into layers, allowing for flexibility in adding or removing layers (e.g., firewalls, load balancers).

5. **Uniform Interface**: Consistent communication structure to access resources, which includes unique URLs for resources and standard formats (e.g., JSON, XML).

6. **Code on Demand (Optional)**: The API can deliver executable code (e.g., JavaScript) that clients can run to enhance functionality.

## Resources in REST APIs

- Resources are fundamental to REST APIs. They represent data that can be manipulated via the API.

| Manager Use Cases         | Endpoint                      |
|---------------------------|-------------------------------|
| View all orders           | `/api/orders`                |
| View a specific order     | `/api/orders/16`             |
| View customer details for an order | `/api/orders/16/customer` |
| View menu items for an order | `/api/orders/16/menu-items` |

| Customer Use Cases        | Endpoint                      |
|---------------------------|-------------------------------|
| Browse all menu items     | `/api/menu-items`            |
| Filter by category        | `/api/menu-items?category=appetizers` |

### Statelessness Revisited

- The server does not remember previous requests. Each call must include necessary parameters. For example, to get menu items for a specific order, the request must specify the order ID explicitly: `/api/orders/16/menu-items`.

### Best Practices for Naming API Endpoints

#### Importance of API Endpoint Design

- **First Impressions Matter**: Well-designed endpoints enhance clarity and usability for developers.
- **Consistency**: Following naming conventions aids in maintainability and collaboration.

## Key Naming Conventions

| Practice                           | Description                                       | Example                           |
|------------------------------------|---------------------------------------------------|-----------------------------------|
| Lowercase Letters                  | Use only lowercase letters for API endpoints      | `/api/menu-items`                |
| Hyphen Usage                       | Separate words with hyphens for readability      | `/api/order-items`               |
| Curly Braces for Variables         | Use camel case for variables in curly braces      | `/api/menu-items/{itemId}`       |
| Hierarchical Relationships          | Use forward slashes to represent resource relationships | `/api/orders/16/menu-items`  |
| Use Nouns for Resources            | Name endpoints with nouns representing the resources | `/api/customers`                |
| Avoid Verbs                        | Use HTTP methods to indicate actions              | `GET /api/orders`                |
| No File Extensions                 | Avoid using file extensions in endpoints          | `/api/users`                     |
| Query String Parameters for Filtering | Use query strings to filter results              | `/api/menu-items?category=appetizers` |
| No Trailing Slashes                | Avoid ending endpoints with a trailing slash      | `/api/orders` (not `/api/orders/`) |

### Recap of Best Practices

- **Use lowercase URI formatting**: Ensures consistency and readability.
- **Indicate hierarchical relationships with a forward slash**: Clearly shows the relationship between resources.
- **Use nouns for resource names**: Makes it clear what the endpoint represents.
- **Avoid file name extensions**: Keep the endpoint clean and let query parameters specify the format.
- **Use query parameters for data types**: Flexibly handle format requests.
- **Don't use a trailing slash**: Avoids confusion and errors.

## Good routes versus bad routes

### Rule 01: Everything in lowercase, with hyphens

| **Good URI Examples**                        | **Status** | **Why**                                   | **Bad URI Examples**                  | **Status** | **Why**                        |
|----------------------------------------------|------------|------------------------------------------|---------------------------------------|------------|-------------------------------|
| `/customers`                                | Good       | Plural and lowercase                     | `/Customers`                         | Bad        | Title case                    |
| `/customers/16/phone-number`                | Good       | Lowercase and hyphen used                | `/generalMembers`                    | Bad        | camelCase, no hyphens         |
| `/customers/16/address/home`                | Good       | Hierarchical with forward slashes        | `/MenuItems`                        | Bad        | Pascal case                    |
| `/users/{userId}`                           | Good       | Variable in camelCase                   | `/customers/16/tel-no`              | Bad        | Abbreviation                   |
|                                              |            |                                          | `/customers/16/phone_number`        | Bad        | Underscores                    |
|                                              |            |                                          | `/customers/16/phonenumber`         | Bad        | No separation of words         |
|                                              |            |                                          | `/users/{user-id}`                   | Bad        | Variable should be camelCase   |

---

### Rule 02: Use a forward slash to indicate a hierarchical relationship

| **Good URI Examples**                                   | **Status** | **Why**                              | **Bad URI Examples**                          | **Status** | **Why**                        |
|---------------------------------------------------------|------------|-------------------------------------|-----------------------------------------------|------------|-------------------------------|
| `/store/customers/{customerId}/orders`                  | Good       | Indicates hierarchical relationship  | `/store/orders/{orderId}/menu-items`        | Good       | Good example                  |
| `/library/authors/books`                                 | Good       | Indicates hierarchical relationship  | `/library/book/{bookId}/isbn`                | Good       | Good example                  |

---

### Rule 03: Use nouns for resource names, not verbs

| **Expects**                | **Good URI Examples**      | **Status** | **Why**                                  | **Bad URI Examples**           | **Status** | **Why**                           |
|----------------------------|----------------------------|------------|-----------------------------------------|--------------------------------|------------|-----------------------------------|
| Collection                 | `/orders`                 | Good       | Uses a noun, not a verb                | `/order`                       | Bad        | Uses singular for collection      |
| Single user                | `/users/{userId}`         | Good       | Proper naming convention                | `/getOrder`                    | Bad        | Uses a verb                       |
|                            |                            |            |                                         | `/getUser/{userId}`           | Bad        | Uses a verb                       |

---

### Rule 04: Avoid special characters

| **Good URI Examples**                       | **Status** | **Why**                               | **Bad URI Examples**                       | **Status** | **Why**                  |
|---------------------------------------------|------------|--------------------------------------|--------------------------------------------|------------|-------------------------|
| `/users/12,23,23/address`                  | Good       | Uses a comma for separation          | `/users/12|23|23/address`                  | Bad        | Special character |     |
|                                             |            |                                      | `/orders/16/menu^items`                   | Bad        | Special character ^     |

---

### Rule 05: Avoid file extensions in URI

| **Good URI Examples**                                   | **Status** | **Why**                               | **Bad URI Examples**                          | **Status** | **Why**                        |
|---------------------------------------------------------|------------|--------------------------------------|-----------------------------------------------|------------|-------------------------------|
| `/sports/basketball/teams/{teamId}?format=json`       | Good       | No file extension                    | `/sports/basketball/teams/{teamId}.json`    | Bad        | File extension at the end     |
| `/assets/js/jquery/3.12/min`                           | Good       | No file extension                    | `/menu-items.json`                           | Bad        | Uses the expected output format as file extension |

---

### Rule 06: Use query parameters to filter when necessary

| **Good URI Examples**                         | **Status** | **Why**                              | **Bad URI Examples**                          | **Status** | **Why**                         |
|-----------------------------------------------|------------|-------------------------------------|-----------------------------------------------|------------|---------------------------------|
| `/users/{userId}/locations`                  | Good       | Hierarchical                        | `/users/{userId}/locations/USA`             | Bad        | Doesn't use a query string      |
| `/users/{userId}/locations?country=USA`     | Good       | Proper use of query string          | `/articles/page/2/items-per-page/10`        | Bad        | Redundant and obscure           |

---

### Rule 07: No trailing slash

| **Good URI Examples**                         | **Status** | **Why**                              | **Bad URI Examples**                        | **Status** | **Why**                     |
|-----------------------------------------------|------------|-------------------------------------|---------------------------------------------|------------|-----------------------------|
| `/users/{userId}`                            | Good       | No trailing slash                   | `/users/{userId}/`                        | Bad        | Trailing slash              |
| `/articles/{articleId}/author`              | Good       | No trailing slash                   | `/articles/{articleId}/author/`           | Bad        | Trailing slash              |

---

This format organizes each rule with corresponding good and bad URI examples for clarity.

### Tools for API Development and Testing

#### Tools Overview

1. **Curl**
   - A command line tool for making HTTP calls, available on all major operating systems.
   - **Usage**:
     - **GET Request**: Type `curl [API URI]` to send a GET request.
     - **POST Request**: Use `curl -X POST -d "[data]" [API URI]` to send a POST request with data.

2. **Postman**
   - A powerful, cross-platform tool for testing and debugging APIs with a user-friendly graphical interface.
   - Offers both desktop and web versions, making it versatile for API development.

3. **Insomnia**
   - A REST API client designed to organize and execute API requests. It’s free and user-friendly.
   - **Setup**:
     - Create a request collection by clicking "Create" and naming it (e.g., "first collection").
     - To create a request, click the Plus icon, choose "HTTP Request," and name it.
     - Select the HTTP method (GET, POST, etc.) and enter the API URL.

#### Practical Demonstration Using Insomnia

- **GET Request**:
  - Use `https://httpbin.org/get?project=LittleLemon`.
  - Click "Send" to view the returned data from httpbin.
  
- **POST Request**:
  - Create a new request, set it to POST, and use `https://httpbin.org/post` as the URL.
  - Use the "Body" tab to input arguments in either Form URL Encoded or JSON format.
  - Input `project` as the argument name and `LittleLemon` as the value, then click "Send" to see the output.

#### Conclusion

- Familiarity with tools like Curl, Postman, and Insomnia will significantly aid in the development and testing of APIs throughout the course.

### Steps for Python Development Setup

#### Step 4: Install Additional VS Code Extensions (Optional)

- **Useful Extensions**:
  - **Python Indent** by Kevin Rose: Helps correct Python indentation in VS Code.
  - **Djaneiro** by Scott Barkman: Provides useful Django snippets.

#### Step 5: Install a Package Manager

- **Install Pipenv**:
  - Pipenv is a package manager for Python applications that simplifies the creation of virtual environments and management of dependencies.
  - **Installation Instructions**:
    1. Open your terminal or PowerShell.
    2. Run the following command:

      ```bash
      pip3 install pipenv
      ```
  
This setup ensures efficient management of your Python projects and their dependencies.

## Creating Django project

**Step 1** : Create a directory for the Django project by running the following command `mkdir LittleLemon`

**Step 2** : Step inside the LittleLemon directory with the command: `cd LittleLemon`

**Step 3** : Run the following command to create a project in this directory: `django-admin startproject BookList .`

**Step 4** : Run a command to activate **pipenv**: `pipenv shell`

**Note** : It is expected that pipenv is installed using pip in your local machine.

**Step 5** : Now run this command to create a Django app: `python manage.py startapp LittleLemonDRF`

**Step 6** : Run the command to start server: `python manage.py runserver`

### Additional resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this section.

- [Curl command line tool and library for transferring data with URLs](https://curl.se/)
- [HTTPie for web and desktop](https://httpie.io/)
- [Postman API platform for building and using APIs](https://www.postman.com/)
- [Postman Echo service to test REST clients and make sample API calls](https://postman-echo.com/)
- [Insomnia homepage](https://insomnia.rest/)
- [Getting started with Insomnia](https://insomnia.rest/)
- [Httpbin HTTP request and response service](https://httpbin.org/)
- [Python Indent by Kevin Rose](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Djaneiro by Scott Barkman](https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [Django](https://www.djangoproject.com/)
- [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
