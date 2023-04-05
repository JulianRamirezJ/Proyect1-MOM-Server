import mysql.connector
from models import config

connection = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
    database=config.DATABASE_NAME
)

def get_connection():
    return connection

def get_cursor():
     return connection.cursor()
