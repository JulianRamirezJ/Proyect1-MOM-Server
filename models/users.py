import mysql.connector
from models.connection import get_connection, get_cursor

class User:
    def __init__(self, id):
        self.id = id
    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM users WHERE id = %s", (id,))
        result = conn.fetchone()
        return User(result[0])
    
    @staticmethod
    def get_all_users():
        conn = get_cursor()
        query = "SELECT * FROM users"
        conn.execute(query)
        result = conn.fetchall()
        return result
    
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO users (id) VALUES (%s)"
            val = (self.id,)
            cursor.execute(sql, val)
            get_connection().commit()
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving user: {e}")
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM users WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
