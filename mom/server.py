from concurrent import futures

import grpc
import config_pb2_grpc
from topics import Topic
from queues import Queue
from users import User

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    config_pb2_grpc.add_TopicServiceServicer_to_server(Topic(), server)
    config_pb2_grpc.add_QueueServiceServicer_to_server(Queue(), server)
    config_pb2_grpc.add_UserServiceServicer_to_server(User(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()