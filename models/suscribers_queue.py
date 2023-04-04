import mysql.connector
from models.connection import get_connection, get_cursor

class SuscriberQueue:
    def __init__(self, queue_id, user_id, id=None):
        self.id = id
        self.queue_id = topic_id
        self.user_id = user_id

    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM suscribers_queue WHERE id = %s", (id,))
        result = conn.fetchone()
        return SuscriberTopic(result[1], result[2], result[0])

    @staticmethod
    def get_all_suscribed_queues_from_user(user_id):
        conn = get_cursor()
        query = "SELECT q.* FROM queues q INNER JOIN suscribers_queue sq ON q.id = sq.queue_id WHERE sq.user_id = %s"
        params = (user_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result


        @staticmethod
    def get_all_suscribed_users_from_queue(queue_id):
        conn = get_cursor()
        query = "SELECT u.* FROM suscribers_queue sq INNER JOIN users u ON sq.user_id = u.id WHERE sq.queue_id = %s"
        params = (queue_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result

    @staticmethod
    def user_is_subscribed(user_id, queue_id):
        conn = get_cursor()
        query = "SELECT * FROM suscribers_queue WHERE queue_id = %s AND user_id = %s"
        params = (queue_id, user_id)
        conn.execute(query, params)
        result = conn.fetchall()
        return len(result) > 0
    
    @staticmethod
    def get_all_suscribed_topics():
        conn = get_cursor()
        query = "SELECT * FROM suscribers_queue"
        conn.execute(query)     
        result = conn.fetchall()
        return result

    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO suscribers_queue (topic_id, user_id) VALUES (%s, %s)"
            val = (self.queue_id, self.user_id)s
            cursor.execute(sql, val)
            get_connection().commit()
        except Exception as e:
            print(f"Error while saving suscriber: {e}") 
        
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM suscribers_queue WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
