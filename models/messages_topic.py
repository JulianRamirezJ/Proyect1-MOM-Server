import mysql.connector
from models.connection import get_connection, get_cursor

class MessageTopicModel:
    def __init__(self, message, topic_queue_id, id=None, status=False):
        self.id = id
        self.message = message
        self.status = status
        self.topic_queue_id = topic_queue_id

    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM messages_topic WHERE id = %s", (id,))
        result = conn.fetchone()
        return MessageTopicModel(result[1], result[3], result[0], result[2])

    @staticmethod
    def get_all_messages_from_topic_queue_not_read(topic_queue_id):
        conn = get_cursor()
        query = """
                    SELECT mt.* FROM messages_topic mt
                    INNER JOIN topics_queue tq ON mt.topic_queue_id = tq.id 
                    WHERE tq.id = %s AND NOT mt.status
                """
        params = (topic_queue_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result
    
    
    @staticmethod
    def get_all_messages():
        conn = get_cursor()
        query = "SELECT * FROM messages_topic"
        conn.execute(query)     
        result = conn.fetchall()
        return result
    
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO messages_topic (message, topic_queue_id) VALUES (%s, %s)"
            val = (self.message, self.topic_queue_id)
            cursor.execute(sql, val)
            get_connection().commit()
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving message: {e}")


    def update_status(self):
        cursor = get_cursor()
        sql = "UPDATE messages_topic SET status = True WHERE id = %s"
        val = (self.id,)
        cursor.execute(sql, val)
        get_connection().commit()
        
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM messages_topic WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
