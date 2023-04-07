from flask import Flask, render_template, request, redirect
from methods.queue import *

def create_queue(request):
    if 'key' in request.headers and 'queue_name' in request.form:
        response = create(request.headers["key"],request.form['queue_name'])
        if response.code == 200:
            return "Queue created sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the queue_name"


def delete_queue(request):
    if 'key' in request.headers and 'queue_name' in request.form:
        response = delete(request.headers["key"],request.form['queue_name'])
        print(response.code)
        if response.code == 200:
            return "Queue deleted sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the queue_name"

def list_queues(request):
    if 'key' in request.headers:
        response = list(request.headers["key"])
        if response.code == 200:
            return "Your queues are {}".format(response.queues)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key"


def subscribe_queue(request):
    if 'key' in request.headers and 'queue_name' in request.form:
        response = subscribe(request.headers["key"],request.form['queue_name'])
        if response.code == 200:
            return "Subscribed to queue {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the queue_name"


def publish_queue(request):
    if 'key' in request.headers and 'queue_name' in request.form and 'message' in request.form:
        response = publish(request.headers["key"],request.form['queue_name'],request.form['message'])
        if response.code == 200:
            return "Published to queue {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the queue_name"


def consume_queue(request):
    if 'key' in request.headers and 'queue_name' in request.form:
        response = consume(request.headers["key"],request.form['queue_name'])
        if response.code == 200:
            return "consumed from queue, message: {}".format(response.message)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the queue_name"