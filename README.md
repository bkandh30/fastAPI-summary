# Asynchronous Text Summarization API

## Overview

This project implements an asynchronous text summarization API developed using Test-Driven Development (TDD). The service exposes RESTful endpoints built with Python and the FastAPI framework, enabling clients to create, retrieve, update, and delete text summaries.

The application leverages modern asynchronous capabilities provided by FastAPI and Tortoise ORM for non-blocking database interactions with a PostgreSQL backend. Docker is utilized for containerization, ensuring consistent development environments and simplifying deployment workflows.

Testing is integral to this project, employing `pytest` for robust unit and integration tests. Continuous Integration (CI) is handled via GitHub Actions, automatically executing the test suite upon commits to ensure code quality before deployment to Heroku.

## Technology Stack

- **Language:** Python 3.x
- **Web Framework:** FastAPI (ASGI)
- **Database:** PostgreSQL (via Docker)
- **ORM:** Tortoise ORM (Asynchronous)
- **Migrations:** Aerich
- **Summarization:** newspaper3k, NLTK
- **Data Validation:** Pydantic
- **Configuration:** Pydantic Settings
- **Containerization:** Docker, Docker Compose
- **Testing Framework:** Pytest, pytest-cov
- **Code Quality:** Black, Flake8, isort

## Key Features

- **RESTful API Design:** Adheres to REST principles using standard HTTP methods for CRUD operations on summaries.
- **Asynchronous Processing:** Built with asynchronous libraries (`FastAPI`, `Tortoise ORM`, `asyncpg`) for high performance, including running blocking summarization tasks in a thread pool.
- **Article Summarization:** Fetches article content from URLs and generates summaries using `newspaper3k`.
- **Database Integration:** Uses Tortoise ORM for efficient async communication with the PostgreSQL database.
- **Database Migrations:** Schema changes managed via Aerich.
- **Containerized Environment:** Fully containerized using Docker and Docker Compose for consistent development and testing (`web` service + `db` service).
- **Configuration Management:** Uses Pydantic Settings for environment-aware configuration (e.g., `DATABASE_URL`).
- **Test-Driven Development:** Developed following TDD principles with Pytest, including unit and integration tests.
- **Code Quality Checks:** Integrated linting, formatting, and coverage reporting.

## API Endpoints

The API provides the following endpoints based on RESTful conventions:

| Endpoint          | HTTP Method | CRUD Operation | Description                       |
| :---------------- | :---------- | :------------- | :-------------------------------- |
| `/summaries`      | `POST`      | CREATE         | Submit a URL to generate summary  |
| `/summaries/{id}` | `GET`       | READ           | Retrieve a specific summary by ID |
| `/summaries`      | `GET`       | READ           | Retrieve all summaries            |
| `/summaries/{id}` | `PUT`       | UPDATE         | Update an existing summary        |
| `/summaries/{id}` | `DELETE`    | DELETE         | Delete a summary by ID            |
| `/ping`           | `GET`       | READ           | Health check endpoint             |

## Getting Started

### Prerequisites

- Docker ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose ([Comes with Docker Desktop or install separately](https://docs.docker.com/compose/install/))

### Running Locally

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bkandh30/fastAPI-summary.git
    cd fastapi-summary/project # Navigate to the directory with docker-compose.yml
    ```

2.  **Build and Start Containers:**

    ```bash
    docker compose up -d --build
    ```

    - This command builds the images for the `web` and `web-db` services (if they don't exist or need updating) and starts them in detached mode.
    - The first time running `web-db` might take a moment to initialize the database. The `web` service's entrypoint script will wait for the database to be ready before starting FastAPI.

3.  **Apply Migrations (Optional but Recommended):** If you pull changes that include new migrations, or to ensure the DB is up-to-date:

    ```bash
    docker compose exec web aerich upgrade
    ```

4.  **Access the API:** The API should now be available at `http://localhost:8004` (or your mapped host port). You can test the ping endpoint: `http://localhost:8004/ping`.

5.  **Stopping the services:**

    ```bash
    docker compose down
    ```

6.  **View Logs:**
    ```bash
    docker compose logs -f web # Follow logs for the web service
    docker compose logs web-db # View logs for the database service
    ```

## Database Migrations

Database schema migrations are handled using [Aerich](https://github.com/tortoise/aerich) (the migration tool for Tortoise ORM). Migration files are stored in the `project/migrations` directory (ensure this is volume mapped in `docker-compose.yml` and committed to Git). Aerich configuration is typically managed in `pyproject.toml`.

**Common Commands:** (Run from the directory containing `docker-compose.yml`, typically `project/`)

- **Initialize Aerich (only once per project):**
  ```bash
  # Ensure pyproject.toml with [tool.aerich] section exists first
  # Or run init and copy the config out of the container
  docker compose exec web aerich init -t app.db.TORTOISE_ORM
  docker compose exec web aerich init-db
  ```
- **Generate Migrations (after changing models in `app/models/tortoise.py`):**
  ```bash
  docker compose exec web aerich migrate --name <migration_name>
  ```
- **Apply Migrations:**
  ```bash
  docker compose exec web aerich upgrade
  ```
- **Show Status:**
  ```bash
  docker compose exec web aerich history
  docker compose exec web aerich heads
  ```

## Code Quality and Linting

This project uses several tools to ensure code quality and style consistency:

- **Black:** For automated code formatting.
- **Flake8:** For linting (style errors, potential bugs).
- **isort:** For automatically sorting Python imports.

Configuration for these tools can often be found in `pyproject.toml`.

### Running Checks Locally

```bash
docker compose exec web flake8 .
docker compose exec web black .
docker compose exec web isort .
```

## Testing and Code Coverage

Testing is performed using pytest and pytest-cov. Both unit and integration tests are included in the project/tests directory.

### Running Tests Locally

Commands are run from the project/ directory.

```bash
# Run all tests

docker compose exec web python -m pytest tests

# Run tests with coverage report

docker compose exec web python -m pytest --cov=app --cov-report=term-missing tests

# Run tests verbosely

docker compose exec web python -m pytest -vv tests

# Run a specific test file or function

docker compose exec web python -m pytest tests/test_summaries.py::test_read_summary
```
