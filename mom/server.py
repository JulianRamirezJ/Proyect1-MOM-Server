from concurrent import futures

import grpc
import config_pb2
import config_pb2_grpc


class Topic(config_pb2_grpc.TopicServiceServicer):
    def create(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def delete(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def listTopics(self, request, context):
        return config_pb2.TopicResponseList(code=200, topics=[])
    def subscribeTopic(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def publishTopic(self, request, context):
        return config_pb2.TopicResponse(code=200)
    def consumeTopic(self, request, context):
        return config_pb2.TopicResponseMessage(code=200, message='')
    
class Queue(config_pb2_grpc.QueueServiceServicer):
    def create(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def delete(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def listTopics(self, request, context):
        return config_pb2.QueueResponseList(code=200, queues=[])
    def subscribeTopic(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def publishTopic(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def consumeTopic(self, request, context):
        return config_pb2.QueueResponseMessage(code=200, message='')

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    config_pb2_grpc.add_TopicServiceServicer_to_server(Topic(), server)
    config_pb2_grpc.add_QueueServiceServicer_to_server(Queue(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
