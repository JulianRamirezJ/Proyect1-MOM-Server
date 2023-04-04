import mysql.connector
from models.connection import get_connection, get_cursor

class SuscriberTopic:
    def __init__(self, topic_id, user_id, id=None):
        self.id = id
        self.topic_id = topic_id
        self.user_id = user_id

    
    @staticmethod
    def get_by_id(id):
        conn = get_cursor()
        conn.execute("SELECT * FROM suscribers_topic WHERE id = %s", (id,))
        result = conn.fetchone()
        return SuscriberTopic(result[1], result[2], result[0])

    @staticmethod
    def get_all_suscribed_topics_from_user(user_id):
        conn = get_cursor()
        query = "SELECT t.* FROM topics t INNER JOIN suscribers_topic st ON t.id = st.topic_id WHERE st.user_id = %s"
        params = (user_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result


    @staticmethod
    def get_all_suscribed_users_from_topic(topic_id):
        conn = get_cursor()
        query = "SELECT u.* FROM suscribers_topic st INNER JOIN users u ON st.user_id = u.id WHERE st.topic_id = %s"
        params = (topic_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result


    @staticmethod
    def user_is_subscribed(user_id, topic_id):
        conn = get_cursor()
        query = "SELECT * FROM subscribers_topic WHERE topic_id = %s AND user_id = %s"
        params = (topic_id, user_id)
        conn.execute(query, params)
        result = conn.fetchall()
        return len(result) > 0
    
    @staticmethod
    def get_all_suscribed_topics():
        conn = get_cursor()
        query = "SELECT * FROM suscribers_topic"
        conn.execute(query)     
        result = conn.fetchall()
        return result

    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO suscribers_topic (topic_id, user_id) VALUES (%s, %s)"
            val = (self.topic_id, self.user_id)
            cursor.execute(sql, val)
            get_connection().commit()
        except Exception as e:
            print(f"Error while saving suscriber: {e}") 
        
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM suscribers_topic WHERE id = %s"
        val = (self.id,)
        conn.execute(sql, val)
        get_connection().commit()
