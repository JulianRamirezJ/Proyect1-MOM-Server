import config_pb2
import config_pb2_grpc
import random
import string

users = []

class User(config_pb2_grpc.UserServiceServicer):
    def Create(self, request, context):
        user_key = (''.join(random.choices(string.ascii_lowercase + string.digits, k=10)))
        insert_user(user_key)
        return config_pb2.UserResponse(code=200, key=user_key)
    

def insert_user(key):
    users.append(key)


def check_key(key):
    return key in users