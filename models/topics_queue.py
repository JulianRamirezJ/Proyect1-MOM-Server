import mysql.connector
from models.connection import get_connection, get_cursor

class TopicsQueueModel:
    def __init__(self, topic_id , suscriber_id, id=None):
        self.id = id
        self.topic_id = topic_id
        self.suscriber_id = suscriber_id
        

    @staticmethod
    def get_by_topic_id_and_suscriber_id(topic_id,suscriber_id):
        conn = get_cursor()
        conn.execute("SELECT * FROM topics_queue WHERE topic_id = %s AND suscriber_id = %s", (topic_id,suscriber_id,))
        result = conn.fetchone()
        return TopicsQueueModel(result[1], result[2], result[0])
    
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO topics_queue (topic_id, suscriber_id) VALUES (%s, %s)"
            val = (self.topic_id, self.suscriber_id)
            cursor.execute(sql, val)
            get_connection().commit()
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving message: {e}")
    