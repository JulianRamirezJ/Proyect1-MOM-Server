import os
import sys
import json
import subprocess
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from client.chasqui import ChasquiConnector
from challenge2.server.config import HOST_MOM, PORT_MOM, USER
# Previously we need create user and put to USER config 

def main():
    conn = ChasquiConnector(HOST_MOM,PORT_MOM, USER)
    while(True):
        message = conn.consume_message_queue(queue_name='queue_request', enable_retry=True)
        data = json.loads(message)
        out = ''
        if data["type"] == "list_files":
            out = subprocess.run('./list_files.sh', stdout=subprocess.PIPE).stdout.decode('utf-8')
        elif data["type"] == "find_files":
            out = subprocess.run(['./find_files.sh',data["name"]], stdout=subprocess.PIPE).stdout.decode('utf-8')
        conn.publish_message_queue(queue_name="queue_response",message=out)
main()