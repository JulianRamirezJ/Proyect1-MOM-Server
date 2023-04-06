import config_pb2
import config_pb2_grpc

class Topic(config_pb2_grpc.TopicServiceServicer):
    def Create(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def Delete(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def ListTopics(self, request, context):
        return config_pb2.TopicResponseList(code=200, topics=[])
    def SubscribeTopic(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def PublishTopic(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def ConsumeTopic(self, request, context):
        return config_pb2.TopicResponseMessage(code=200, message='')