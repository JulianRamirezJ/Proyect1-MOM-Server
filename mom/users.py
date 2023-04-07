import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
import config_pb2
import config_pb2_grpc
import random
import string
from models.users import UserModel
users = []

class User(config_pb2_grpc.UserServiceServicer):
    def Create(self, request, context):
        user_key = (''.join(random.choices(string.ascii_lowercase + string.digits, k=10)))
        insert_user(user_key)
        user = UserModel(user_key)
        user.save()
        return config_pb2.UserResponse(code=200, key=user_key)

def insert_user(key):
    users.append(key)

def check_key(key):
    return key in users

def runBackup():
    users_bd = UserModel.get_all_users()
    for user in users_bd:
        insert_user(user[0])

runBackup()
print(users)