from config.connection_grpc import stub_topic
from config import config_pb2

def create(key, topic_name):
    return stub_topic.Create(config_pb2.TopicRequest(key=key,topic_name=topic_name))

def delete(key, topic_name):
    return stub_topic.Delete(config_pb2.TopicRequest(key=key,topic_name=topic_name))

def list(key):
    return stub_topic.ListTopics(config_pb2.TopicRequest(key=key))

def subscribe(key, topic_name):
    return stub_topic.SubscribeTopic(config_pb2.TopicRequest(key=key,topic_name=topic_name))

def publish(key, topic_name, message): 
    return stub_topic.PublishTopic(config_pb2.TopicRequestMessage(key=key,topic_name=topic_name,message=message))

def consume(key, topic_name): 
    return stub_topic.ConsumeTopic(config_pb2.TopicRequest(key=key,topic_name=topic_name))

