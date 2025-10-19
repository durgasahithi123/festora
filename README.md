# Celebrating India's Heritage 🇮🇳

A full-stack web application designed to showcase the rich cultural tapestry of India, from ancient traditions to vibrant festivals. This project is built with a decoupled frontend and a powerful Flask API backend.

## 📑 Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)

  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Usage](#usage)
  - [Running the Application](#running-the-application)

- [API Endpoints](#api-endpoints)

## About The Project

This interactive cultural portal provides a dynamic and engaging user experience for exploring India's heritage. The application features a clean, modern frontend that communicates with a robust Flask backend to serve data on festivals, temples, spiritual books, and traditional foods. It includes a complete user authentication system, allowing users to sign up, log in, and have a personalized session.

The project is architected using professional web development patterns, including a decoupled frontend, an API-first backend, the application factory pattern, and database migrations.

---

## Key Features

- **Dynamic Content**: All cultural data is loaded dynamically from the database via REST APIs.
- **User Authentication**: Secure user signup, login, and session management.
- **API-Driven**: A decoupled frontend consumes data from a well-defined Flask REST API.
- **Database Integration**: Uses SQLite with Flask-SQLAlchemy for data persistence.
- **Schema Management**: Employs Flask-Migrate to handle database schema changes gracefully.
- **Responsive UI**: A clean user interface that showcases the cultural information beautifully.

---

## Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Migrate
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Environment**: Python Virtual Environment (`venv`)

---

## Project Structure

The project follows a scalable and maintainable structure, separating concerns into logical directories.

```
/festora_backend/
│
├── app.py              # Main application factory
├── extensions.py       # Decoupled Flask extensions (db, migrate)
├── seed.py             # Script to populate the database with sample data
│
├── models/             # SQLAlchemy database models
│   └── db_models.py
│
├── routes/             # Flask Blueprints for different routes
│   ├── auth_routes.py  # Handles /api/signup, /api/login, etc.
│   ├── data_routes.py  # Handles /api/festivals, /api/books, etc.
│   └── view_routes.py  # Renders the HTML pages
│
├── static/             # All static assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/          # All HTML files
│
├── migrations/         # Flask-Migrate versioning folder
│
├── .env                # Environment variables (SECRET_KEY)
├── requirements.txt    # Python dependencies
└── database.db         # The SQLite database file
```

---

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

- Python 3.8+ and Pip installed on your system.

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/durgasahithi123/festora
    cd your-repo-name/festora_backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the venv
    python -m venv venv

    # Activate it (on macOS/Linux)
    source venv/bin/activate

    # On Windows:
    # venv\Scripts\activate
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the environment file:**
    Create a file named `.env` in the `festora_backend` directory and add a secret key:

    ```
    SECRET_KEY='a-very-long-and-random-string-for-security'
    ```

5.  **Set up the Flask environment:**
    Create a file named `.flaskenv` and add the following lines. This tells the `flask` command how to find your app.

    ```
    FLASK_APP=app.py
    FLASK_DEBUG=1
    ```

6.  **Initialize and migrate the database:**
    These commands will create your `database.db` file and all the necessary tables.

    ```bash
    # 1. Initialize the migrations folder (run only once)
    flask db init

    # 2. Generate the initial migration script
    flask db migrate -m "Initial migration"

    # 3. Apply the migration to create the tables
    flask db upgrade
    ```

---

## Usage

### Seeding the Database

Before running the app, populate the database with some sample data using the provided seed script.

```bash
python seed.py
```

### Running the Application

Start the Flask development server:

```bash
python app.py
```

Your application will be running at **`http://127.0.0.1:5000`**. Open this URL in your web browser to see the project live.

---

## API Endpoints

The backend provides the following REST API endpoints.

### Authentication API

| Endpoint      | Method | Description                                |
| :------------ | :----- | :----------------------------------------- |
| `/api/signup` | `POST` | Creates a new user account.                |
| `/api/login`  | `POST` | Authenticates a user and starts a session. |
| `/api/logout` | `POST` | Terminates the current user session.       |
| `/api/status` | `GET`  | Checks if a user is currently logged in.   |

### Data API

| Endpoint         | Method | Description                               |
| :--------------- | :----- | :---------------------------------------- |
| `/api/festivals` | `GET`  | Returns a JSON list of all festival data. |
| `/api/books`     | `GET`  | Returns a JSON list of all book data.     |
| `/api/temples`   | `GET`  | Returns a JSON list of all temple data.   |
| `/api/foods`     | `GET`  | Returns a JSON list of all food data.     |
