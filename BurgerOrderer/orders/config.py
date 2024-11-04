"""
Configuration file for Flask application 
"""
import MySQLdb

HOST = "db"
USER = "root"
PASSWORD = "password"
DATABASE = "burger"
PORT = 3306


def create_database_if_not_exists():
    """
    Create the MYSQL database if it doesn't exist.
    """
    connection = MySQLdb.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        port=PORT
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
    cursor.close()
    connection.close()

DATABASE_URL = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

class Config:
    SECRET_KEY = "very_very_secret_key"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False