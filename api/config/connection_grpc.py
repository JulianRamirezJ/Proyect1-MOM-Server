import grpc
import config.config_pb2_grpc as config_pb2_grpc
connection = grpc.insecure_channel('localhost:50051')
stub_topic = config_pb2_grpc.TopicServiceStub(connection)
stub_queue = config_pb2_grpc.QueueServiceStub(connection)