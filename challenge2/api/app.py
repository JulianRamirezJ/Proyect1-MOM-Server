import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from client.chasqui import ChasquiConnector
from challenge2.server.config import HOST_MOM, PORT_MOM, USER
from flask import Flask, render_template, request, redirect
import config
import json
#Setup our app
app = Flask(__name__)

conn = ChasquiConnector(HOST_MOM,PORT_MOM, USER)


@app.route("/list_files")
def list_files():
    data = {
        "type": "list_files"
    }
    conn.publish_message_queue("queue_request", json.dumps(data),)
    message = conn.consume_message_queue("queue_response", True)
    return message

@app.route("/find_files", methods=["POST"])
def find_files():
    data = {
        "type": "find_files",
        "name": request.form["name"]
    }
    conn.publish_message_queue("queue_request", json.dumps(data), )
    message = conn.consume_message_queue("queue_response", True)
    return message

if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)