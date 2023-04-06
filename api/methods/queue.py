from config.connection_grpc import stub_queue
from config import config_pb2

def create(key, queue_name):
    return stub_queue.Create(config_pb2.QueueRequest(key=key,queue_name=queue_name))

def delete(key, queue_name):
    return stub_queue.Delete(config_pb2.QueueRequest(key=key,queue_name=queue_name))

def list(key):
    return stub_queue.ListQueues(config_pb2.QueueRequest(key=key))

def subscribe(key, queue_name):
    return stub_queue.SubscribeQueue(config_pb2.QueueRequest(key=key,queue_name=queue_name))

def publish(key, queue_name, message): 
    return stub_queue.PublishQueue(config_pb2.QueueRequestMessage(key=key,queue_name=queue_name,message=message))

def consume(key, queue_name): 
    return stub_queue.ConsumeQueue(config_pb2.QueueRequest(key=key,queue_name=queue_name))

