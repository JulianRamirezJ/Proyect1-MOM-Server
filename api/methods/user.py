from config.connection_grpc import stub_user
from config import config_pb2

def create():
    return stub_user.Create(config_pb2.Null())