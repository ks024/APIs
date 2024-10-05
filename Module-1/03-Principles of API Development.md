# Principles of API development

## REST API Best Practices

1. **Keep It Simple (KISS)**:
   - Design APIs to perform specific tasks well.
   - **Example**: For the Little Lemon project, separate the processes of updating the item of the day into two API calls:
     - Update the current item to "Off" (e.g., `PATCH menu-items/16` with status set to "Off").
     - Manually select a new item and update its status to "On" (e.g., `PATCH menu-items/21` with status set to "On").

2. **Filtering, Ordering, and Pagination**:
   - **Filtering**: Allow clients to filter results using query parameters (e.g., by course type).
   - **Ordering**: Enable clients to specify the order of results (ascending or descending) via query parameters (e.g., `GET menu-items?sort=price&order=asc`).
   - **Pagination**: Implement pagination to return smaller chunks of data, improving performance and usability (e.g., `GET menu-items?page=10&limit=4`).

3. **Versioning**:
   - Use versioning to prevent breaking changes in client applications. Support a maximum of two versions to avoid complexity.

4. **Caching**:
   - Implement caching to reduce database load. Use relevant HTTP headers to manage cache behavior.
   - **Example**: Cache results for `GET menu-items` and serve cached data for repeated requests until a modification occurs.

5. **Rate Limiting and Monitoring**:
   - Apply rate limiting to control the number of API calls from a user over a specified time period.
   - Monitor API performance by tracking latency, status codes (particularly 400-499 and 500-599), and network bandwidth to ensure optimal operation and identify issues early.

By adhering to these best practices—simplicity, filtering, ordering, pagination, versioning, caching, and monitoring—you'll create robust and sustainable APIs.

### API Security Best Practices

1. **Importance of API Security**:
   - APIs make data accessible to applications and third-party clients, which increases utility but also poses risks to back-end services. Securing APIs is crucial to protect server and database access.

2. **SSL (Secure Socket Layer)**:
   - **Encryption**: Use SSL to encrypt data transmitted between the browser and server.
   - **Implementation**: Set up SSL certificates from a reputable provider to serve APIs over HTTPS. Always ensure that API endpoints begin with HTTPS.

3. **Signed URLs**:
   - **Purpose**: Ensure that API calls originate from authorized sources (e.g., specific mobile applications or websites).
   - **Mechanism**: Use signed URLs that include a signature with each API call, verified by server-side code.
   - **HMAC**: A common signing mechanism that uses a secret key and a digest algorithm to generate the signature.

4. **Authentication**:
   - **Token-Based Authentication**: Prefer this over traditional username and password methods. Users authenticate once to receive a unique token.
   - **Token Usage**: Include the token in the HTTP header for subsequent API calls, allowing the server to validate the user without repeatedly sending credentials.
   - **Standards**: Consider using industry-standard tokens like JSON Web Tokens (JWT).

5. **HTTP Status Codes**:
   - **401 Unauthorized**: Indicates that the username and password do not match, preventing access.
   - **403 Forbidden**: Means credentials are valid, but the user lacks permission to perform the requested action.

6. **CORS (Cross-Origin Resource Sharing)**:
   - Control which domains can access your API by configuring CORS headers, allowing calls from specific domains only.

7. **Firewalls**:
   - Use firewall applications to restrict API access to specific IP addresses, adding an additional layer of security.

By implementing these security measures—SSL, signed URLs, token-based authentication, understanding HTTP status codes, CORS, and firewalls—you can significantly enhance the security of your APIs and protect user data.

### Access Control in API Design

1. **Importance of Access Control**:
   - Protects sensitive data (e.g., customer delivery addresses) by ensuring that only authorized users (managers and delivery crew) can access specific APIs.
   - Limits visibility of sensitive information to prevent unauthorized access.

2. **Roles and Privileges**:
   - **Roles**: Collections of privileges that define what a user can do.
   - **Privileges**: Specific tasks a user is allowed to perform.

   **Example Roles for the Little Lemon API**:
   - **Customer Role**:
     - Browse menu items
     - Add items to the cart
     - Place orders
     - Add food reviews
     - View their own orders
   - **Manager Role**:
     - Add, edit, and delete menu items
     - Browse all orders
     - Access customer data
     - Assign orders to delivery crew
     - View transaction data
   - **Delivery Crew Role**:
     - Browse assigned orders
     - Update order statuses

3. **Role Complexity**:
   - Different roles (e.g., administrators, HR accounts) can be created, each with tailored privileges.
   - More detailed privileges lead to a more effective access control system.

4. **Authentication vs. Authorization**:
   - **Authentication**: Verifies user identity (who you are).
   - **Authorization**: Determines what an authenticated user is allowed to do (what you can do).

5. **Managing Multiple Roles**:
   - Users may need access to multiple roles. Options for handling this:
     - **Single Comprehensive Role**: Create one role that encompasses all essential privileges (e.g., a general manager with all accountant and manager privileges).
     - **Multiple Task-Specific Roles**: Assign multiple roles to users (e.g., a general manager can have roles for accountant, HR, and manager), ensuring they have access to all necessary functions.

6. **Dynamic Privilege Assignment**:
   - If privileges change (e.g., adding a new privilege to the accountant role), users with multiple roles automatically receive these updates.

7. **Benefits of Effective Access Control**:
   - Saves time and reduces the need for costly debugging and refactoring.
   - A well-designed access control system enhances overall project efficiency and security.

By investing time in planning roles and privileges, you create a robust access control system that benefits developers and the project as a whole.

### Authentication vs. Authorization in API Security

#### Introduction

Securing APIs is essential as they provide third-party clients access to backend data. Without proper security, sensitive information can be exposed or tampered with. Authentication and authorization are two critical concepts for controlling access to your API endpoints.

---

#### Authentication

- **Definition**: The process of verifying a user's credentials.
- **Example**: Logging into a website using a username and password. Upon successful login, the system sets cookies in the browser, which are sent with subsequent requests to authenticate the user without requiring them to log in again.

**Token-Based Authentication Process**:

1. The client provides credentials (username and password).
2. The API server issues a bearer token.
3. The client includes this token in every API call.

- If the credentials are invalid, the server responds with a **401 Unauthorized** status code.

**Analogy**: Authentication is like receiving an employee card after submitting your paperwork on your first day at work. The employee card allows you to enter the building, similar to how authentication allows access to the API.

The two steps in the API authentication process can be represented by the following two diagrams.

**Authentication process: Getting an access token**
![Authentication process: Getting an access token](authentication1.png)

**Authenticated API calls**
![Authenticated API calls](authentication2.png)

#### Authorization

- **Definition**: Determines what an authenticated user can do. It checks if the user has the necessary privileges to perform specific actions.
  
**Process**:

- After authentication, the server checks if the user belongs to the appropriate group or role to perform the requested task.
- If the user does not have the required privileges, the server responds with a **403 Forbidden** status code.

**API authorization**
![API authorization](authorization.png)

**Analogy**: Even with an employee card, access to certain rooms may be restricted. Authorization dictates what areas (or API features) a user can access.

---

#### Implementing Authorization

1. **Identify Privileges**: Define the specific tasks users can perform. Example privileges for a bookshop:
   - Browse books
   - Add new books
   - Edit books
   - Delete books
   - Place orders

2. **Role Assignment**: Distribute these privileges into roles (e.g., Manager, Editor, Customer). Each role will have specific privileges assigned.

3. **Backend Check**: In the backend code, verify if an authenticated user belongs to the required role before allowing access to certain actions.

---

#### User Groups in Django

- **Django Admin Panel**: Provides a robust user group system where you can create roles (e.g., Manager, Editor) and assign privileges.
- **Managing Privileges**: Easily add or remove privileges from groups as your project evolves.

**Example**:

- Create an **Editor** role with privileges to edit books.
- Create a **Customer** role with limited privileges, such as browsing books and placing orders.

**Implementation**: After defining user groups and assigning users, you'll need to implement checks in your API views to ensure users have the correct permissions.

---

By understanding and effectively implementing authentication and authorization, you can secure your API endpoints and protect sensitive data while ensuring that users have appropriate access based on their roles.
