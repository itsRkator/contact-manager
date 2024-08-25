# Contact Manager

## Overview

This project is a Django-based application using Alembic for database migrations and SQLAlchemy for ORM. It includes a variety of tools and configurations to manage and deploy the application effectively.

## Folder Structure

```plaintext
.venv
alembic/
  versions/
    5acc5e3bb92b_create_contacts_table.py
  env.py
  README
  script.py.mako
api/
  management/
    commands/
      populate_data.py
  __init__.py
  admin.py
  apps.py
  models.py
  serializers.py
  sqlalchemy.py
  tests.py
  urls.py
  utils.py
  views.py
contact_manager/
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py
alembic.ini
manage.py
requirements.txt
```

## Prerequisites

1. **Python**: Ensure you have Python 3.8 or later installed.
2. **Virtual Environment**: Use a virtual environment to manage dependencies.

## Setup

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Edit `alembic.ini` to set the `sqlalchemy.url` with your database connection string.

Example:

```ini
sqlalchemy.url = postgresql://username:password@localhost/databasename
```

### 5. Database Migrations

To initialize the database with the current migrations:

```bash
alembic upgrade head
```

To create a new migration after modifying models:

```bash
alembic revision --autogenerate -m "description_of_changes"
```

To apply the new migration:

```bash
alembic upgrade head
```

## Development

### Running the Django Server

Start the development server with:

```bash
python manage.py runserver
```

### Running Tests

To run tests:

```bash
python manage.py test
```

### Custom Management Commands

To use custom management commands (e.g., populate data):

```bash
python manage.py populate_data
```

### Application Structure

- **`api/`**: Contains the core application logic and configurations.
  - **`models.py`**: Define your data models here.
  - **`serializers.py`**: Define serializers for API data transformation.
  - **`views.py`**: Define views for handling requests.
  - **`urls.py`**: Define URL routing for the `api` app.
  - **`tests.py`**: Write tests for your application.
  - **`utils.py`**: Utility functions used across the app.
  - **`sqlalchemy.py`**: SQLAlchemy configuration and setup.
  - **`management/commands/`**: Custom Django management commands.
- **`contact_manager/`**: Contains Django project settings and configurations.
  - **`settings.py`**: Project settings.
  - **`urls.py`**: Project URL routing.
  - **`wsgi.py`**: WSGI configuration for deployment.
  - **`asgi.py`**: ASGI configuration for asynchronous support.

## Configuration Files

- **`alembic.ini`**: Alembic configuration for migrations.
- **`manage.py`**: Django management script for running commands.
- **`requirements.txt`**: Lists the Python packages required for the project.

## Logging

Logging is configured in `alembic.ini`. The logs will be output to the console by default.

## Contributing

If you’d like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code follows the project’s style guidelines and passes all tests.

## License

This project is licensed under the [MIT License](LICENSE).