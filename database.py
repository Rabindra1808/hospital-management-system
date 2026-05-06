import os

import mysql.connector


def get_connection():
    """
    Create a MySQL connection.

    On hosted environments (e.g., Streamlit Cloud), `localhost` refers to the app container,
    not your local MySQL. Use environment variables to configure the real DB host.
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "R@1234bin"),
        database=os.getenv("DB_NAME", "hospital_db"),
        port=int(os.getenv("DB_PORT", "3306")),
    )
