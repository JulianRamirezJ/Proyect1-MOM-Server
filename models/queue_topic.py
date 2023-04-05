import mysql.connector
from models.connection import get_connection, get_cursor

class MessageQueue:
    def __init__(self, message, queue_id, id=None):
        self.id = id
        self.message = message
        self.queue_id = queue_id

    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM messages_queue WHERE id = %s", (id,))
        result = conn.fetchone()
        return Topic(result[1], result[2], result[0])

    @staticmethod
    def get_all_messages_from_queue(queue_id):
        conn = get_cursor()
        query = "SELECT * FROM messages_queue WHERE queue_id = %s"
        params = (queue_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result
    
    @staticmethod
    def get_all_messages():
        conn = get_cursor()
        query = "SELECT * FROM messages_queue"
        conn.execute(query)     
        result = conn.fetchall()
        return result
    
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO messages_queue (message, queue_id) VALUES (%s, %s)"
            val = (self.message, self.queue_id)
            cursor.execute(sql, val)
            get_connection().commit()
        except Exception as e:
            print(f"Error while saving message: {e}") 
        
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM messages_queue WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
