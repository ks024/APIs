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

## Consequences of a poorly designed API project

| **Consequences of a Poorly Designed API Project** | **Reasons** | **Consequences** | **Fix** |
|---------------------------------------------------|-------------|------------------|---------|
| **Data Breach**                                   | Poor security checks, no authentication/authorization, improper file permissions, no SSL | Sensitive data leaks, financial damage, trust issues | Implement proper security checks, create a solid authorization layer, ensure SSL usage. |
| **Data Corruption**                               | Poor security, no authentication/authorization, absence of data validation/sanitization | Unexpected data modifications, severe data corruption/loss | Validate and sanitize user data, establish a strong authorization layer. |
| **Wastage of Computing Power and Memory**        | Unoptimized code, improper business logic, lack of validation, unoptimized SQL queries, no caching | Increased costs, slow system performance | Optimize code and database queries, implement caching, check for inefficiencies before deployment. |
| **Wastage of Bandwidth**                          | Absence of caching headers, lack of caching policies, no pagination/filtering | Increased costs, poor API performance, excessive resource consumption by client apps | Use proper caching headers, implement pagination and filtering features. |
| **Bad User Experience**                           | Poor naming conventions, incorrect HTTP codes, lack of features like pagination/searching | Steeper learning curve, additional processing for clients, unexpected errors | Follow standard conventions, ensure proper error handling, implement essential API features. |
| **Breaking Client Applications**                  | Poor versioning management | Backward compatibility issues, client apps may stop working | Maintain a proper versioning system to ensure backward compatibility. |
| **Failure to Manage the App**                     | Overloading a single app, placing all logic in views | Unmanageable codebase, slow feature addition, poor performance | Distribute functionalities across smaller apps, encapsulate business logic in models. |

### Conclusion

Properly designing an API from the start is crucial for long-term success. The repercussions of a poorly designed API affect all users, including both API developers and client application developers. Use this guide to ensure successful API projects in the future.

### Note: JSON and XML Response Types

When building APIs, it's essential to allow clients to request their preferred content type—either **JSON** or **XML**—via the `Accept` header in the request. This gives clients flexibility in how they handle and display the returned data.

#### Request Headers for Content Type

Clients can specify the desired format in the `Accept` header of their HTTP request:

- **JSON**: `Accept: application/json`
- **XML**: `Accept: application/xml` or `Accept: text/xml`

For example, an API request with the `Accept: application/json` header will return data in JSON format, while a request with `Accept: application/xml` will return the data in XML format.

#### Data Conversion with Django REST Framework (DRF)

In this course, you'll build APIs using **Django REST Framework (DRF)**, which comes with built-in renderers for converting data into different formats. DRF typically supports rendering data to **JSON** by default but also allows easy conversion to **XML** and **YAML** through third-party renderer classes.

#### JSON vs XML

- **JSON (JavaScript Object Notation)**:
  - Lightweight, simple, and widely used.
  - Easily parsed and generated in most programming languages.
  - Preferred by JavaScript developers due to native support as a JavaScript object.

- **XML (Extensible Markup Language)**:
  - More complex, tag-based format similar to HTML.
  - Can represent more complex and hierarchical data.
  - Allows inclusion of metadata through attributes and supports comments.

#### Comparison Table

| Feature                   | JSON                                           | XML                                          |
|---------------------------|------------------------------------------------|----------------------------------------------|
| **Size**                   | Smaller, uses less bandwidth                  | Larger, uses more bandwidth                  |
| **Structure**              | Key-value pairs                               | Tag-based, no key-value pairs                |
| **Arrays**                 | Easily represented as arrays                  | Verbose representation using multiple tags  |
| **Processing Speed**       | Faster to generate and parse                  | Slower, more memory-intensive                |
| **Comments**               | No comments allowed                           | Allows comments                             |
| **Readability**            | Simple and compact, easy for humans to read   | Can be more readable, but more verbose       |

#### Example

- **JSON Format:**

  ```json
  {
    "author": "Jack London",
    "title": "Seawolf"
  }
  ```

- **XML Format:**

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <root>
     <author>Jack London</author>
     <title>Seawolf</title>
  </root>
  ```

- **JSON Array Example:**

  ```json
  {
    "items": [1, 2, 3, 4, 5]
  }
  ```

- **XML Array Example:**

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <root>
     <items>
       <element>1</element>
       <element>2</element>
       <element>3</element>
       <element>4</element>
       <element>5</element>
     </items>
  </root>
  ```

- **JSON** is more lightweight and efficient for data exchange, making it the default choice in modern web APIs.
- **XML** is more powerful and flexible, supporting attributes and complex hierarchical data, but it is generally more verbose and computationally intensive.

Throughout this course, you'll primarily use **JSON** for API responses due to its simplicity and efficiency, but you'll also be able to handle **XML** when needed.

## Debugging in Visual Studio Code: A Quick Guide

Debugging is a crucial skill for any developer, as it allows you to identify and fix errors in your code efficiently. Visual Studio Code (VS Code) offers powerful built-in debugging tools that help you understand how your program works and resolve issues faster.

### Setting Up the Debugger in VS Code

1. **Activate the Virtual Environment**:  
   Open the terminal in VS Code and activate your project's virtual environment by running:

   ```bash
   pipenv shell
   ```

2. **Open the Project in VS Code**:  
   Once the environment is activated, open your project in VS Code. From the command palette, select the appropriate Python interpreter for the project.

3. **Create a New Django App**:  
   If you haven't already, create a new Django app in your project and open it in VS Code.

4. **Access the Debugger**:  
   On the left sidebar, find the **Debugger icon** and click on it. This will open the **Debug panel**. If this is your first time using the debugger, you'll see a "Create a `launch.json` file" link at the top of the panel.

5. **Configure the Debugger for Django**:  
   Click on the **Create a `launch.json` file** link, which will open a list of available configurations. Select **Django** from this list, and the debugger will be configured to work with your Django project.

#### Running the Debugger

Once the configuration is complete, you can run your Django app with the debugger. There are two options:

- **Start Debugging**: This will start the debugger and automatically activate your virtual environment. The Django web server will be launched automatically.
- **Run Without Debugging**: This option runs the application without attaching the debugger.

#### Key Debugging Concepts

1. **Breakpoints**:  
   - A **breakpoint** is a point in your code where execution is paused. You can set a breakpoint by clicking the red dot next to the line number in the code editor. This allows you to examine the values of variables at that point in time.
   - To remove a breakpoint, simply click the red dot again.

2. **Watch**:  
   - The **Watch** feature lets you keep track of the values of specific variables as the code executes. You can add a variable to the watch list by clicking the **+** icon in the **Watch** section of the Debug panel.
   - This is helpful for monitoring changes in variables over time and helps in identifying issues like incorrect values.

#### Debug Toolbar

When the debugger is paused at a breakpoint, a debug toolbar becomes visible. It contains six buttons:

1. **Continue (F5)**: Resumes the execution of the program until the next breakpoint is reached or the program finishes.
2. **Pause**: Pauses the execution of the program if it's running.
3. **Step Over (F10)**: Executes the current line of code and pauses on the next line. It skips over function calls.
4. **Step Into (F11)**: If the current line contains a function call, this will take you into that function and pause at the first line of the function.
5. **Step Out (Shift+F11)**: If you're inside a function, this will take you back to the line where the function was called and pause there.
6. **Restart**: Restarts the current debugging session from the beginning.
7. **Stop**: Stops the debugging session and the web server.

#### Example: Debugging a Simple Django View

1. **Add Code to `views.py`**:  
   Suppose you are trying to display even numbers in your Django app. You create a route that triggers a function that is supposed to display even numbers. However, when you access the route, nothing displays in the browser. This indicates that something is wrong.

2. **Set a Breakpoint**:  
   Set a breakpoint at line 9 of the view function. Start the debugger and revisit the endpoint in the browser.

3. **Debugger Doesn’t Pause**:  
   The debugger doesn't pause at line 9, meaning that the value of `remainder` is never `0`. You then add the `remainder` variable to the **Watch** list by clicking on the **+** icon in the **Watch** section.

4. **Step Through the Code**:  
   After adding the variable to the watch list, you step through the code, and notice that the value of `remainder` increases by `0.5`, which should not happen. This indicates that something is wrong with the calculation.

5. **Fix the Error**:  
   After inspecting line 7, you realize that the **division operator** was mistakenly used instead of the **modulo operator**. You fix the code by replacing `/` with `%` (the modulo operator).

6. **Restart the Debugging Session**:  
   Remove all breakpoints, restart the debugging session, and revisit the endpoint. Now, the function works as expected, and only even numbers are displayed in the browser.

In this guide, you learned the basics of how to use the built-in debugger in Visual Studio Code to efficiently find and fix errors in your code. Debugging is an essential skill that helps you:

- Identify and understand errors faster.
- Monitor variable values at different stages of code execution.
- Step through your code and isolate the exact point where things go wrong.

By mastering debugging, you’ll significantly reduce the time spent on troubleshooting and improve your development workflow.

## Useful Tools in Your Browser's Developer Console for Debugging API Calls

Every modern browser provides a **developer console** with powerful tools for debugging, including monitoring API requests made from JavaScript on websites. Below is a guide to help you use the **Chrome Developer Console** effectively to debug your API calls.

### Opening the Developer Console

- **Windows/Linux**: Press **Ctrl + Shift + I**.
- **MacOS**: Press **Cmd + Option + I**.

The developer console is an essential tool when debugging API calls made via JavaScript on your website.

### Key Features of the Developer Console

1. **Network Tab**:
   - The **Network Tab** lets you inspect all network requests (including API calls) made from your website.
   - To focus on API calls, click the **Fetch/XHR filter** to narrow down the view to API requests specifically.

2. **Making an API Call**:
   - Open the **Console** tab in the Developer Console.
   - You can initiate an **HTTP GET request** to your API using JavaScript's `fetch` function. For example:

     ```javascript
     fetch('https://api.example.com/data')
       .then(response => response.json())
       .then(data => console.log(data));
     ```

   - After pressing **Enter**, go to the **Network** tab to view the request and its associated response.

3. **Inspecting API Calls**:
   - In the **Network** tab, the API call is recorded and you can click on it to inspect the details.
     - **Headers**: In the **Headers** tab, you can see all the request and response headers for the API call.
     - **Preview**: The **Preview** tab shows the formatted output of the API response.
     - **Response**: The **Response** tab shows the raw output (unformatted) of the API response.

4. **Initiator Tab**:
   - The **Initiator** tab shows the exact line in your JavaScript code where the API call was initiated. This is helpful for tracing the source of the request in your code.

5. **Disable Cache Option**:
   - Just below the **Network** tab, there's a checkbox labeled **Disable cache**.
   - If you want to ensure you get fresh data from your APIs (without using cached responses), keep this box checked. This prevents the browser from using any cached response.

6. **Recording and Clearing Network Calls**:
   - All the API calls made by your JavaScript will be logged in the **Network** tab. You can click on individual calls to inspect them.
   - To clear all recorded network calls, click the **Clear** button next to the red record button.

#### Inspecting a Public API

For example, to inspect a public API like `https://restcountries.com/v3.1/all`:

- Visit the API endpoint directly in the browser. It returns a list of countries in **JSON** format.
- By default, JSON responses in the browser appear as raw, unformatted text. This makes it harder to read.

#### Formatting JSON Output

- **Install a JSON Formatter Extension**:
  - To format JSON output in your browser, install a **JSON Formatter** extension from your browser’s extension store (available for Chrome, Firefox, etc.).
  - After installing and enabling the extension, revisit the API endpoint (`https://restcountries.com/v3.1/all`). The output will now be displayed in a neatly formatted structure, making it easier to read and debug.

The browser's **Developer Console** is a powerful tool for debugging API requests made by JavaScript. The **Network Tab** is especially useful for inspecting API calls in detail, allowing you to examine headers, responses, and where the API call originated in your code. Additionally, installing a **JSON Formatter** extension can make working with JSON data much more manageable.

These tools help you debug and optimize API interactions on your website more efficiently.

## Mock APIs

**Mock APIs** are simulated API endpoints that return fake data, allowing client developers to start building applications before the real API is live. They speed up development by providing a way for both API and client developers to work in parallel.

- **How it works**: Mock APIs mimic real endpoints with pre-generated data. Client developers can integrate and test their apps without waiting for the real API, and once the real API is ready, they can switch the mock endpoints with actual ones.
  
- **Benefits**: Faster development, reduced dependencies between API and client developers, and smoother transitions when moving to real APIs.

**Steps**:

1. Create fake data.
2. Create mock API endpoints that return this data.

**Popular Tools**:

- **[Mockaroo](http://www.mockaroo.com/)** for generating fake data.
- **[MockAPI](https://mockapi.io/)** for creating mock API endpoints.

Mock APIs play a vital role in reducing development time and improving workflow efficiency by allowing parallel development.

## Module Review: RESTful API Development

Congratulations! You've completed the module on **RESTful API Development**. Here’s a summary of the key concepts and topics you’ve learned:

### 1. **APIs in the Real World**

- You learned how APIs are used in real-world applications, with insights from Meta software engineer Celina Florentin.

### 2. **HTTP and HTTPS Basics**

- **HTTP**: The communication protocol between a client (e.g., browser) and a server.
- **HTTPS**: A more secure version of HTTP, where data is encrypted on both the client and server sides.
- **HTTP Methods**: You were reminded of the main HTTP methods like **GET**, **POST**, **PUT**, and **DELETE**. For example, **PUT** is used to update an entire resource.

### 3. **HTTP Requests, Responses, and Status Codes**

- You refreshed your understanding of **HTTP requests** and **responses**, and you covered the most commonly used status codes (e.g., 200, 404, 500).

### 4. **RESTful Principles and Naming Conventions**

- **REST**: You learned that REST (Representational State Transfer) is an architectural style for designing APIs, and an API is considered RESTful only if it follows specific constraints. One key constraint is that REST APIs are **stateless**.
- **Naming Conventions**: You learned the importance of consistent naming conventions for endpoints to improve clarity and maintainability. For example, use **nouns** (e.g., `/books`) for resources and **avoid verbs**.

### 5. **API Development Tools**

- **Insomnia**: A popular free REST API client that allows you to test APIs with an easy-to-use interface.
- You gained hands-on experience setting up your tools and environment for API development.

### 6. **API Principles: Best Practices, Security, Authentication, and Access Control**

- **REST Best Practices**: You learned that it's important to limit the number of versions (no more than two) for any given resource.
- **API Security**: You explored security best practices such as **signed URLs** to limit access to resources and **token-based authentication** to avoid exposing usernames and passwords in every request.
- **Access Control**: You learned how to set **roles and privileges** to ensure that only authorized users can access specific data.

### 7. **Project Setup**

- You learned about organizing your API projects effectively, such as splitting large Django apps into smaller, manageable ones. For instance, creating separate apps when upgrading an API to prevent breaking existing functionality.

### 8. **XML and JSON Response Types**

- You learned about **JSON** and **XML**, the two most common response formats used in APIs. JSON is simpler and lighter, while XML supports more complex structures and is often more readable.

### 9. **Debugging APIs**

- You practiced debugging your Python scripts using **VS Code’s built-in debugger**. This tool is essential for troubleshooting and improving your API development workflow.

### 10. **Mock APIs**

- You learned how to use **Mock APIs** to simulate real API endpoints with fake data, allowing client developers to build and test their applications even before the actual API is live. This helps speed up the development process by reducing dependencies between the API and client developers.
- Popular **Mock API Tools**:
  - **[Mockaroo](http://www.mockaroo.com/)** (for fake data generation).
  - **[MockAPI](https://mockapi.io/)** (for creating mock API endpoints).
