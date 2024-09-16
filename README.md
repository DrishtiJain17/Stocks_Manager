# Stock Management Web Application

This is a simple full-stack web application built with HTML, CSS, JavaScript, Flask and PostgreSQL that allows users to manage a list of stocks. Users can create, read, update, and delete stock entries. Additionally, the application supports user authentication and role-based access control using Flask-Security.

## Features
- User Authentication (Login, Registration)
- CRUD Operations: Easily create, read, update, and delete stock entries.
- Secure password hashing and authentication tokens
- Role-based access control
- Basic front-end using HTML, CSS, and JavaScript and Bootstrap for designing.
- PostgreSQL as the database : Store and manage detailed stock information, including name, ticker symbol, and price.
- Pagination: Efficiently view and manage large lists of stocks with pagination features.
- Responsive Design: Access Stockify from any device with a modern, responsive web design.
- User-friendly and efficient: The application is well-structured and easy to navigate.

## Technologies Used
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: PostgreSQL
- Authentication: Flask-Security

## Prerequisites

Before running this project locally, ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Git

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/DrishtiJain17/Stocks_Manager.git
cd .\Stocks_Manager\
```


### 2. Install Dependencies

Run the following command to install all the required dependencies:

```bash
pip install -r req.txt
```

This will install Flask, Flask-Security, psycopg2, and other required libraries.

### 3. Set Up PostgreSQL Database

Make sure PostgreSQL is running on your system. Create a database for the application:

1. Open PostgreSQL shell and Login with your PostgreSQL credentials.
2. Create the database:
   ```bash
   CREATE DATABASE stocks_db;
   ```
3. Exit the shell:
   ```bash
   \q
   ```

### 4. Configure the Application

Ensure that the PostgreSQL connection settings in the `config.py` file match your PostgreSQL credentials.

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://yourusername:yourpassword@localhost/stocks_db'
```


### 5. Run the Application

Now, you can start the Flask application by running:

```bash
python app.py
```

By default, the app will run on `http://127.0.0.1:5000/`.

### 6. Access the Application

Once the app is running, you can access it by opening your browser and navigating to:

```
http://127.0.0.1:5000/
```

You will be able to:
- Register a new account
- Log in
- Perform CRUD operations on stocks
- Use pagination to browse through vaious stock entries
- Log out

## Additional Features

- **Role Management**: Some routes are restricted based on user roles.
- **Authentication**: Token-based and session-based authentication is used.
- **CSRF Protection**: Security features are enabled for handling CSRF attacks.

## Other Features
- **Pagination**: Implement pagination to handle large lists of stocks.
- **Bootstrap**: Add Bootstrap for better UI design and responsiveness.

## Troubleshooting

- If the application cannot connect to PostgreSQL, ensure that the database is running and that your credentials (username/password) are correct.
- If `psycopg2` fails to install, try installing the PostgreSQL development libraries on your system:
  - For Ubuntu/Debian:
    ```bash
    sudo apt-get install libpq-dev python3-dev
    ```

---
