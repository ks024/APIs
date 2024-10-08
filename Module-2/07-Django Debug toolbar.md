# Integrating Django Debug Toolbar

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
