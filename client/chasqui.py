import requests
import json
import time

class ChasquiConnector:

    def __init__(self, host, port, user=None):
        self.HOST = host
        self.PORT = port
        if user:
            self.user = user
        else:
            self.user = self.create_user()
            print(f"Your key is {self.user}")

    def _make_request(self, method, endpoint, key=None, payload=None):
        url = f"http://{self.HOST}:{self.PORT}/{endpoint}"
        headers = {}
        if key:
            headers["key"] = key
        if payload:
            response = requests.request(method, url, headers=headers, data=payload)
        else:
            response = requests.request(method, url, headers=headers)
        return response.text

    def get_user_key(self):
        return self.user

    def create_user(self):
        return self._make_request("GET", "create_user")

    def create_topic(self, topic_name):
        payload = {"topic_name": topic_name}
        return self._make_request("POST", "create_topic", key=self.user, payload=payload)

    def create_queue(self, queue_name):
        payload = {"queue_name": queue_name}
        return self._make_request("POST", "create_queue", key=self.user, payload=payload)

    def list_topics(self):
        return self._make_request("POST", "list_topics", key=self.user)

    def list_queues(self):
        return self._make_request("POST", "list_queues", key=self.user)

    def delete_topic(self, topic_name):
        payload = {"topic_name": topic_name}
        return self._make_request("POST", "delete_topic", key=self.user, payload=payload)

    def delete_queue(self, queue_name):
        payload = {"queue_name": queue_name}
        return self._make_request("POST", "delete_queue", key=self.user, payload=payload)

    def subscribe_topic(self, topic_name):
        payload = {"topic_name": topic_name}
        return self._make_request("POST", "subscribe_topic", key=self.user, payload=payload)

    def subscribe_queue(self, queue_name):
        payload = {"queue_name": queue_name}
        return self._make_request("POST", "subscribe_queue", key=self.user, payload=payload)

    def publish_message_topic(self, topic_name, message):
        payload = {"topic_name": topic_name, "message": message}
        return self._make_request("POST", "publish_topic", key=self.user, payload=payload)

    def publish_message_queue(self, queue_name, message):
        payload = {"queue_name": queue_name, "message": message}
        return self._make_request("POST", "publish_queue", key=self.user, payload=payload)

    def consume_message_topic(self, topic_name, enable_retry):
        payload = {"topic_name": topic_name}
        if enable_retry:
            while True:
                response = self._make_request("POST", "consume_topic", key=self.user, payload=payload)
                if response != 'Request returned error code 400':
                        return response
                time.sleep(1)
        else:
            return self._make_request("POST", "consume_topic", key=self.user, payload=payload)

    def consume_message_queue(self, queue_name, enable_retry):
        payload = {"queue_name": queue_name}
        if enable_retry:
            while True:
                response = self._make_request("POST", "consume_queue", key=self.user, payload=payload)
                if response != 'Request returned error code 400':
                        return response
                time.sleep(1)
        else:
            return self._make_request("POST", "consume_queue", key=self.user, payload=payload)