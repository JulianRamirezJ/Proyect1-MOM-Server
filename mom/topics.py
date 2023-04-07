import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
import config_pb2
import config_pb2_grpc
from users import check_key
from models.topics import TopicModel
from models.topics_queue import TopicsQueueModel
from models.messages_topic import MessageTopicModel

topics = {}

class Topic(config_pb2_grpc.TopicServiceServicer):


    def Create(self, request, context):
        if (check_key(request.key) and request.topic_name not in list(topics.keys())):
            topics[request.topic_name] = {'creator': request.key, 'queues': {request.key: []}}
            print(topics)
            topic = TopicModel(request.topic_name,request.key)
            topic.save()
            topic_queue = TopicsQueueModel(topic.id,request.key)
            topic_queue.save()
            return config_pb2.TopicResponse(code=200)
        return config_pb2.TopicResponse(code=500)
    

    def Delete(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_creator(request.key, request.topic_name)):
                del topics[request.topic_name]
                print(topics)
                topic = TopicModel(request.topic_name,request.key)
                topic.delete()
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
                topic = TopicModel.get_by_name(request.topic_name)
                topic_queue = TopicsQueueModel(topic.id,request.key)
                topic_queue.save()
                return config_pb2.TopicResponse(code=200)
            return config_pb2.TopicResponse(code=400)
        return config_pb2.TopicResponse(code=500)
    

    def PublishTopic(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_subscriber(request.key, request.topic_name)):
                topic = TopicModel.get_by_name(request.topic_name)
                for queue in topics[request.topic_name]['queues']:
                    if(queue != request.key):
                        topics[request.topic_name]['queues'][queue].append(request.message)
                        topic_queue = TopicsQueueModel.get_by_topic_id_and_suscriber_id(topic.id, queue)
                        message_topic = MessageTopicModel(request.message, topic_queue.id)
                        message_topic.save()
                        topics[request.topic_name]['message_ids'][queue].append(message_topic.id)
                print(topics)
                return config_pb2.TopicResponse(code=200)
            return config_pb2.TopicResponse(code=400)
        return config_pb2.TopicResponse(code=500)
    

    def ConsumeTopic(self, request, context):
        if (check_key(request.key) and request.topic_name in list(topics.keys())):
            if(is_subscriber(request.key, request.topic_name)):
                message = topics[request.topic_name]['queues'][request.key].pop(0)
                message_topic_id = topics[request.topic_name]['message_ids'][request.key].pop(0)
                message_topic = MessageTopicModel.get_by_id(message_topic_id)
                message_topic.update_status()
                print(topics)
                return config_pb2.TopicResponseMessage(code=200, message=message)
            return config_pb2.TopicResponseMessage(code=400, message='')
        return config_pb2.TopicResponseMessage(code=500, message='')
    

def is_creator(key, topic_name):
    return topics[topic_name]['creator'] == key

def is_subscriber(key, topic_name):
    return key in list(topics[topic_name]['queues'].keys())

def runBackup():
    topics_bd = TopicModel.get_all_topics()
    for topic in topics_bd:
        print(topic)
        topics[topic[1]] = {'creator': topic[2], 'queues': {}, 'message_ids':{}}
        newTopic = TopicModel(topic[1],topic[2],topic[0])
        topics_queue_bd = newTopic.get_all_suscribed_users()
        for topic_queue in topics_queue_bd:
            print(topic_queue,'topic_queue')
            topics[topic[1]]['queues'][topic_queue[2]] = []
            topics[topic[1]]['message_ids'][topic_queue[2]] = []
            messages_topic_bd = MessageTopicModel.get_all_messages_from_topic_queue_not_read(topic_queue[0])
            for message in messages_topic_bd:
                topics[topic[1]]['queues'][topic_queue[2]].append(message[1])
                topics[topic[1]]['message_ids'][topic_queue[2]].append(message[0])

runBackup()
print(topics)