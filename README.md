# FastAPI Social Media API

A robust, scalable, and efficient RESTful API for a basic social media application developed using Python's FastAPI framework.

## Features

* User Management - Register, Login, and Profile Management.
* Posts - Create, Update, Delete, and Fetch Posts.
* Votes - Upvote or Downvote Posts.
* Schema Validation - Using Pydantic Models.
* Authentication and Authorization - Secure routes with JWT.

## Tech Stack

* FastAPI - For building the API.
* SQLAlchemy - SQL Toolkit and ORM.
* Pydantic - Data Validation and Settings Management.
* JWT - For Secure Authentication.
* Pytest - For Testing.
* GitHub Actions - CI/CD.

## Getting Started

### Prerequisites

* Python 3.8 or higher

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-social-media.git
cd fastapi-social-media
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Run the server

```bash
uvicorn main:app --reload
```

### Testing

To run the tests, use the following command:

```bash
pytest
```

## Structure

Here's a basic folder structure and file organization for your FastAPI social media API project:

```bash
/fastapi-social-media
|-- /app
|   |-- /main
|   |   |-- __init__.py
|   |   |-- main.py
|   |-- /models
|   |   |-- __init__.py
|   |   |-- user.py
|   |   |-- post.py
|   |-- /schemas
|   |   |-- __init__.py
|   |   |-- user.py
|   |   |-- post.py
|   |-- /routes
|   |   |-- __init__.py
|   |   |-- user.py
|   |   |-- post.py
|   |-- /services
|   |   |-- __init__.py
|   |   |-- auth.py
|-- /tests
|   |-- test_main.py
|   |-- test_auth.py
|   |-- /fixtures
|   |   |-- __init__.py
|   |   |-- db.py
|-- .env
|-- .gitignore
|-- README.md
|-- pyproject.toml
|-- poetry.lock
|-- .github
|   |-- /workflows
|   |   |-- ci.yml
```

Here's what each part does:

* `main.py` is the entry point to your application.
* The `models` folder contains your SQLAlchemy models.
* The `schemas` folder contains your Pydantic models for serialization/deserialization and validation.
* The `routes` folder contains the route definitions for your API.
* The `services` folder contains any additional services your application uses, such as authentication.
* The `tests` folder is where your Pytest tests live. The `fixtures` folder within `tests` contains your Pytest fixtures.
* `.env` is where you'll put your environment variables.
* `.gitignore` is a list of files and directories that should not be tracked by Git.
* `README.md` is a markdown file containing information about your project.
* `pyproject.toml` is the configuration file for Poetry. It contains metadata about the project and its direct dependencies.
* `poetry.lock` is an auto-generated file that contains the exact versions of your dependencies that your project should use. Each developer who clones the project will get these same versions, ensuring that the project behaves the same everywhere.
* The `.github/workflows` folder contains your GitHub Actions workflows, such as your CI/CD pipeline.