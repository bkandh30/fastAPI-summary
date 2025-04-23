# Asynchronous Text Summarization API

## Overview

This project implements an asynchronous text summarization API developed using Test-Driven Development (TDD). The service exposes RESTful endpoints built with Python and the FastAPI framework, enabling clients to create, retrieve, update, and delete text summaries.

The application leverages modern asynchronous capabilities provided by FastAPI and Tortoise ORM for non-blocking database interactions with a PostgreSQL backend. Docker is utilized for containerization, ensuring consistent development environments and simplifying deployment workflows.

Testing is integral to this project, employing `pytest` for robust unit and integration tests. Continuous Integration (CI) is handled via GitHub Actions, automatically executing the test suite upon commits to ensure code quality before deployment to Heroku.

## Technology Stack

- **Language:** Python 3.x
- **Web Framework:** FastAPI (Asynchronous)
- **Database:** PostgreSQL
- **ORM:** Tortoise ORM (Asynchronous)
- **Containerization:** Docker
- **Testing Framework:** Pytest
- **CI/CD:** GitHub Actions
- **Deployment Platform:** Heroku

## Key Features

- **RESTful API Design:** Adheres to REST principles using standard HTTP methods for CRUD operations.
- **Asynchronous Processing:** Built entirely with asynchronous libraries (`FastAPI`, `Tortoise ORM`) for high performance and concurrency.
- **Test-Driven Development:** Developed following TDD methodology to ensure reliability and maintainability.
- **Containerized Environment:** Dockerized for ease of setup and deployment consistency.
- **Database Interaction:** Utilizes an asynchronous ORM for efficient communication with the Postgres database.
- **Automated Testing & Deployment:** Integrates with GitHub Actions for CI and facilitates streamlined deployment to Heroku.

## API Endpoints

The API provides the following endpoints based on RESTful conventions:

| Endpoint          | HTTP Method | CRUD Operation | Description                       |
| :---------------- | :---------- | :------------- | :-------------------------------- |
| `/summaries`      | `GET`       | READ           | Retrieve all summaries            |
| `/summaries/{id}` | `GET`       | READ           | Retrieve a specific summary by ID |
| `/summaries`      | `POST`      | CREATE         | Add a new text summary            |
| `/summaries/{id}` | `PUT`       | UPDATE         | Update an existing summary by ID  |
| `/summaries/{id}` | `DELETE`    | DELETE         | Delete a summary by ID            |
