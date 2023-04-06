import config_pb2
import config_pb2_grpc

class Queue(config_pb2_grpc.QueueServiceServicer):
    def Create(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def Delete(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def ListQueues(self, request, context):
        return config_pb2.QueueResponseList(code=200, queues=[])
    def SubscribeQueue(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def PublishQueue(self, request, context):
        return config_pb2.QueueResponse(code=200)
    def ConsumeQueue(self, request, context):
        return config_pb2.QueueResponseMessage(code=200, message='')