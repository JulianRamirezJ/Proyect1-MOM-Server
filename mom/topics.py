import config_pb2
import config_pb2_grpc
from users import check_key

topics = {}

class Topic(config_pb2_grpc.TopicServiceServicer):


    def Create(self, request, context):
        if (check_key(request.key) and request.topic_name not in list(topics.keys())):
            topics[request.topic_name] = {'creator': request.key, 'queues': {request.key: []}}
            print(topics)
            return config_pb2.TopicResponse(code=200)
        return config_pb2.TopicResponse(code=500)
    

    def Delete(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_creator(request.key, request.topic_name)):
                del topics[request.topic_name]
                print(topics)
                return config_pb2.TopicResponse(code=200)
        return config_pb2.TopicResponse(code=500)
    

    def ListTopics(self, request, context):
        if (check_key(request.key)):
            topic_response = []
            for key in topics:
                if topics[key]['creator'] == request.key:
                    topic_response.append(key)
            print(topics)
            return config_pb2.TopicResponseList(code=200, topics=topic_response)
        return config_pb2.TopicResponseList(code=500, topics=[])
    

    def SubscribeTopic(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(not is_subscriber(request.key, request.topic_name)):
                topics[request.topic_name]['queues'][request.key] = []
                print(topics)
                return config_pb2.TopicResponse(code=200)
            return config_pb2.TopicResponse(code=400)
        return config_pb2.TopicResponse(code=500)
    

    def PublishTopic(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_subscriber(request.key, request.topic_name)):
                for queue in topics[request.topic_name]['queues']:
                    if(queue != request.key):
                        topics[request.topic_name]['queues'][queue].append(request.message)
                print(topics)
                return config_pb2.TopicResponse(code=200)
            return config_pb2.TopicResponse(code=400)
        return config_pb2.TopicResponse(code=500)
    

    def ConsumeTopic(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_subscriber(request.key, request.topic_name)):
                message = topics[request.topic_name]['queues'][request.key].pop(0)
                print(topics)
                return config_pb2.TopicResponseMessage(code=200, message=message)
            return config_pb2.TopicResponseMessage(code=400, message='')
        return config_pb2.TopicResponseMessage(code=500, message='')
    

def is_creator(key, topic_name):
    return topics[topic_name]['creator'] == key

def is_subscriber(key, topic_name):
    return key in list(topics[topic_name]['queues'].keys())