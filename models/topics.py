import mysql.connector
from models.connection import get_connection, get_cursor

class TopicModel:
    def __init__(self, name, user_id, id=None):
        self.id = id
        self.name = name
        self.user_id = user_id

    
    @staticmethod
    def get_by_name(name):
        conn = get_cursor()
        conn.execute("SELECT * FROM topics WHERE name = %s", (name,))
        result = conn.fetchone()
        return TopicModel(result[1], result[2], result[0])

    @staticmethod
    def get_all_topics_from_user(user_id):
        conn = get_cursor()
        query = "SELECT * FROM topics WHERE user_id = %s"
        params = (user_id,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result
    
    @staticmethod
    def get_all_topics():
        conn = get_cursor()
        query = "SELECT * FROM topics"
        conn.execute(query)     
        result = conn.fetchall()
        return result

    def get_name(self):
        return self.name


    def get_all_suscribed_users(self):
        conn = get_cursor()
        query = """
                    SELECT tq.* FROM topics_queue tq INNER JOIN users u 
                    ON tq.suscriber_id = u.id INNER JOIN topics t 
                    ON tq.topic_id = t.id WHERE t.name = %s
                """
        params = (self.name,)
        conn.execute(query, params)
        result = conn.fetchall()
        return result

    def user_is_subscribed(self, suscriber_id):
        conn = get_cursor()
        query = """
                    SELECT * FROM topics_queue 
                    JOIN topics ON topics_queue.topic_id = topics.id 
                    WHERE topics.name = %s AND suscriber_id = %s
                """
        params = (self.name, suscriber_id)
        conn.execute(query, params)
        result = conn.fetchall()
        return len(result) > 0
    
    def save(self):
        try:
            cursor = get_cursor()
            sql = "INSERT INTO topics (name, user_id) SELECT %s, %s WHERE NOT EXISTS (SELECT 1 FROM topics WHERE name = %s) LIMIT 1"
            val = (self.name, self.user_id, self.name)
            cursor.execute(sql, val)
            get_connection().commit()
            self.id = cursor.lastrowid
        except Exception as e:
            print(f"Error while saving user: {e}")
        
        
    def delete(self):
        conn = get_cursor()
        sql = "DELETE FROM topics WHERE name = %s"
        val = (self.name,)
        conn.execute(sql, val)
        get_connection().commit()
