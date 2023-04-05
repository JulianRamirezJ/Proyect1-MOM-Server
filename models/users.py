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

    def get_all_suscribed_topics(self):
        conn = get_cursor()
        query = "SELECT t.* FROM topics t INNER JOIN suscribers_topic st ON t.id = st.topic_id WHERE st.user_id = %s"
        params = (self.id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result   

    def get_all_suscribed_queues(self):
        conn = get_cursor()
        query = "SELECT q.* FROM queues q INNER JOIN suscribers_queue sq ON q.id = sq.queue_id WHERE sq.user_id = %s"
        params = (self.id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result
    
    def suscribe_topic(self, topic_id):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO suscribers_topic (topic_id, user_id) VALUES (%s, %s)"
            val = (topic_id, self.id)
            cursor.execute(sql, val)
            get_connection().commit()
        except Exception as e:
            print(f"Error while saving suscriber: {e}") 

    def suscribe_queue(self, queue_id):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO suscribers_queue (queue_id, user_id) VALUES (%s, %s)"
            val = (queue_id, self.id)
            cursor.execute(sql, val)
            get_connection().commit()
        except Exception as e:
            print(f"Error while saving suscriber: {e}") 

    def desuscribe_topic(self, topic_id):
        conn = get_cursor()
        sql = "DELETE FROM suscribers_topic WHERE user_id = %s AND topic_id = %s"
        val = (self.id, topic_id)
        conn.execute(sql, val)
        get_connection().commit()

    def desuscribe_queue(self, queue_id):
        conn = get_cursor()
        sql = "DELETE FROM suscribers_queue WHERE user_id = %s AND queue_id = %s"
        val = (self.id, queue_id)
        conn.execute(sql, val)
        get_connection().commit()

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