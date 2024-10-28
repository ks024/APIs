# Little Lemon API

## Overview

The Little Lemon API provides endpoints for managing a restaurant's menu items, orders, and user roles. This API is designed to facilitate interactions for various user types including managers, delivery crew, and customers.

### Project Description

| **Title**          | **Little Lemon API**                                         |
|--------------------|-------------------------------------------------------------|
| **Overview**       | A RESTful API for managing restaurant operations including menu items, orders, and user roles. |
| **Features**       | - User registration and authentication<br>- Role-based access control<br>- Cart management<br>- Order management<br>- Filtering, pagination, and sorting capabilities<br>- API throttling |
| **Project Structure** | - **Django App:** LittleLemonAPI<br>- **Dependencies:** Managed with `pipenv` |

### API Endpoints

| **Category**              | **Endpoint**                         | **Method** | **Role**                     | **Purpose**                                         |
|---------------------------|-------------------------------------|------------|------------------------------|-----------------------------------------------------|
| **User Management**       | `/api/users`                       | POST       | No role required             | Create a new user                                   |
|                           | `/api/users/users/me/`            | GET        | Anyone with a valid token    | Retrieve current user details                        |
|                           | `/token/login/`                    | POST       | Anyone with valid credentials | Generate access tokens                               |
| **Menu Items**           | `/api/menu-items`                  | GET        | Customer, Delivery Crew      | List all menu items                                 |
|                           | `/api/menu-items`                  | POST       | Manager                      | Create a new menu item                              |
|                           | `/api/menu-items/{menuItem}`       | GET        | Manager                      | Retrieve a single menu item                         |
|                           | `/api/menu-items/{menuItem}`       | PUT/PATCH  | Manager                      | Update a menu item                                  |
|                           | `/api/menu-items/{menuItem}`       | DELETE     | Manager                      | Delete a menu item                                  |
| **User Group Management** | `/api/groups/manager/users`        | GET        | Manager                      | List all managers                                   |
|                           | `/api/groups/manager/users`        | POST       | Manager                      | Assign a user to the manager group                  |
|                           | `/api/groups/manager/users/{userId}` | DELETE   | Manager                      | Remove a user from the manager group                |
| **Cart Management**       | `/api/cart/menu-items`             | GET        | Customer                     | Retrieve current cart items                          |
|                           | `/api/cart/menu-items`             | POST       | Customer                     | Add an item to the cart                             |
|                           | `/api/cart/menu-items`             | DELETE     | Customer                     | Clear the user's cart                               |
| **Order Management**      | `/api/orders`                      | GET        | Customer                     | Retrieve all orders for the user                    |
|                           | `/api/orders`                      | POST       | Customer                     | Create a new order                                  |
|                           | `/api/orders/{orderId}`            | GET        | Customer                     | Retrieve order details                               |
|                           | `/api/orders/{orderId}`            | PUT/PATCH  | Manager                      | Update an order                                     |
|                           | `/api/orders/{orderId}`            | DELETE     | Manager                      | Delete an order                                     |
|                           | `/api/orders`                      | Delivery Crew | GET                          | Retrieve orders for the delivery crew               |
|                           | `/api/orders/{orderId}`            | PATCH      | Delivery Crew                | Update order status                                  |

### Error Handling

| **HTTP Status Code** | **Reason**                                |
|----------------------|-------------------------------------------|
| 200                  | OK                                        |
| 201                  | Created                                   |
| 400                  | Bad Request                               |
| 401                  | Unauthorized                              |
| 403                  | Forbidden                                 |
| 404                  | Not Found                                 |

### Throttling

| **Description**      | **Details**                               |
|----------------------|-------------------------------------------|
| **Throttling**       | Manages request rates for authenticated and unauthenticated users. |

### Getting Started

| **Step**                | **Command**                             |
|-------------------------|-----------------------------------------|
| Install dependencies     | `pipenv install`                       |
| Run the application      | `pipenv run python manage.py runserver`|

### Conclusion

| **Description**        | **Details**                             |
|------------------------|-----------------------------------------|
| **Overview**           | Comprehensive API for restaurant operations. Use endpoints to integrate efficiently. |
