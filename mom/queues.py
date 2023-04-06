import config_pb2
import config_pb2_grpc
from users import check_key

queues = {}

class Queue(config_pb2_grpc.QueueServiceServicer):

    def Create(self, request, context):
        if (check_key(request.key) and request.queue_name not in list(queues.keys())):
            queues[request.queue_name] = {'creator': request.key, 'queue': [], 'subscribers':[request.key]}
            print(queues)
            return config_pb2.QueueResponse(code=200)
        return config_pb2.QueueResponse(code=500)
    

    def Delete(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_creator(request.key,request.queue_name)):
                del queues[request.queue_name]
                print(queues)
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
                return config_pb2.QueueResponse(code=200)
            return config_pb2.QueueResponse(code=400)
        return config_pb2.QueueResponse(code=500)
    

    def PublishQueue(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_subscriber(request.key, request.queue_name)):
                queues[request.queue_name]['queue'].append(request.message)
                print(queues)
                return config_pb2.QueueResponse(code=200)
            return config_pb2.QueueResponse(code=400)
        return config_pb2.QueueResponse(code=500)
    

    def ConsumeQueue(self, request, context):
        if (check_key(request.key) and request.queue_name in list(queues.keys())):
            if(is_subscriber(request.key, request.queue_name)):
                message = queues[request.queue_name]['queue'].pop(0)
                print(queues)
                return config_pb2.QueueResponseMessage(code=200, message=message)
            return config_pb2.QueueResponseMessage(code=400, message='')
        return config_pb2.QueueResponseMessage(code=500, message='')
    

def is_creator(key, queue_name):
    return queues[queue_name]['creator'] == key

def is_subscriber(key, queue_name):
    return key in queues[queue_name]['subscribers']