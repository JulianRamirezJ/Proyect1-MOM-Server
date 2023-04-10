import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from client.chasqui import ChasquiConnector
from challenge2.server.config import HOST_MOM, PORT_MOM, USER
# Previously we need create user and put to USER config 

def main():
    conn = ChasquiConnector(HOST_MOM,PORT_MOM,USER)
    conn.create_queue('queue_request')
    conn.create_queue('queue_response')
main()