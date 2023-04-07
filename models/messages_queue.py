import mysql.connector
from models.connection import get_connection, get_cursor

class MessageQueue:
    def __init__(self, message, queue_id, id=None, status=False):
        self.id = id
        self.message = message
        self.status = status
        self.queue_id = topic_id

    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM messages_queue WHERE id = %s", (id,))
        result = conn.fetchone()
        return MessageQueue(result[1], result[3], result[0], result[2])

    @staticmethod
    def get_all_messages_from_queue(queue_id):
        conn = get_cursor()
        query = "SELECT * FROM messages_queue WHERE queue_id = %s"
        params = (queue_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result

    @staticmethod
    def get_all_messages_from_queue(queue_name):
        conn = get_cursor()
        query = """
                SELECT mq.* FROM messages_queue mq 
                INNER JOIN queues q ON mq.queue_id = q.id 
                WHERE q.name = %s
            """
        params = (queue_name,)
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
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving message: {e}")
    
    def update_status(self):
        cursor = get_cursor()
        sql = "UPDATE messages_queue SET status = True WHERE id = %s"
        val = (self.id,)
        cursor.execute(sql, val)
        get_connection().commit()


    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM messages_queue WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
