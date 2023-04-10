import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
import config_pb2
import config_pb2_grpc
from users import check_key, users
from models.queues import QueueModel
from models.suscribers_queue import SuscribersQueueModel
from models.messages_queue import MessageQueueModel

queues = {}

class Queue(config_pb2_grpc.QueueServiceServicer):

    def Create(self, request, context):
        if (check_key(request.key) and request.queue_name not in list(queues.keys())):
            queues[request.queue_name] = {'creator': request.key, 'queue': [], 'subscribers':[request.key], 'message_ids': []}
            print(queues)
            queue = QueueModel(request.queue_name,request.key)
            queue.save()
            subscribers_queue_model = SuscribersQueueModel(request.key,queue.id) 
            subscribers_queue_model.save()
            return config_pb2.QueueResponse(code=200)
        return config_pb2.QueueResponse(code=500)
    

    def Delete(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_creator(request.key,request.queue_name)):
                del queues[request.queue_name]
                print(queues)
                queue = QueueModel(request.queue_name, request.key)
                queue.delete()
                return config_pb2.QueueResponse(code=200)
        return config_pb2.QueueResponse(code=500)
    

    def ListQueues(self, request, context):
        if (check_key(request.key)):
            queue_response = []
            for key in queues:
                if queues[key]['creator'] == request.key:
                    queue_response.append(key)
            print(queues)
            return config_pb2.QueueResponseList(code=200, queues=queue_response)
        return config_pb2.QueueResponseList(code=500, queues=[])
    

    def SubscribeQueue(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(not is_subscriber(request.key, request.queue_name)):
                queues[request.queue_name]['subscribers'].append(request.key)
                print(queues)
                queue = QueueModel.get_by_name(request.queue_name)
                subscribers_queue_model = SuscribersQueueModel(request.key,queue.id) 
                subscribers_queue_model.save()
                return config_pb2.QueueResponse(code=200)
            return config_pb2.QueueResponse(code=400)
        return config_pb2.QueueResponse(code=500)
    

    def PublishQueue(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_subscriber(request.key, request.queue_name)):
                queues[request.queue_name]['queue'].append(request.message)
                queue = QueueModel.get_by_name(request.queue_name)
                message_queue = MessageQueueModel(request.message, queue.id)
                message_queue.save()
                queues[request.queue_name]['message_ids'].append(message_queue.id)
                print(queues)
                return config_pb2.QueueResponse(code=200)
            return config_pb2.QueueResponse(code=400)
        return config_pb2.QueueResponse(code=500)
    

    def ConsumeQueue(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_subscriber(request.key, request.queue_name)):
                if(len(queues[request.queue_name]['queue']) > 0):
                    message = queues[request.queue_name]['queue'].pop(0)
                    message_queue_id = queues[request.queue_name]['message_ids'].pop(0)
                    message_queue = MessageQueueModel.get_by_id(message_queue_id)
                    message_queue.update_status()
                    print(queues)
                    return config_pb2.QueueResponseMessage(code=200, message=message)
            return config_pb2.QueueResponseMessage(code=400, message='')
        return config_pb2.QueueResponseMessage(code=500, message='')
    

def is_creator(key, queue_name):
    return queues[queue_name]['creator'] == key

def is_subscriber(key, queue_name):
    return key in queues[queue_name]['subscribers']

def runBackup():
    queues_bd = QueueModel.get_all_queues()
    for queue in queues_bd:
        newQueue = QueueModel(queue[1],queue[2],queue[0])
        subscribers = []
        messages = []
        message_ids = []
        subscribers_bd = newQueue.get_all_suscribed_users()
        messages_bd = MessageQueueModel.get_all_messages_from_queue_not_read(newQueue.name)
        for subscriber in subscribers_bd:
            subscribers.append(subscriber[0])
        for message in messages_bd:
                messages.append(message[1])
                message_ids.append(message[0])
        queues[newQueue.name] = {'creator': newQueue.user_id, 'queue': messages, 'subscribers': subscribers, 'message_ids': message_ids }

runBackup()
print(queues)