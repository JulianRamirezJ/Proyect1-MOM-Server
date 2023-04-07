import mysql.connector
from models.connection import get_connection, get_cursor

class SuscribersQueueModel:
    def __init__(self, subscriber_id, queue_id, id=None):
        self.id = id
        self.queue_id = queue_id
        self.suscriber_id = subscriber_id
        
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO suscribers_queue (queue_id, suscriber_id) VALUES (%s, %s)"
            val = (self.queue_id, self.suscriber_id)
            cursor.execute(sql, val)
            get_connection().commit()
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving message: {e}")