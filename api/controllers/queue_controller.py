from flask import Flask, render_template, request, redirect
from methods.queue import *

def create_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        response = create(request.headers["key"],request.form['queue_name'])
        print(response.code)
        return "create queue"
    else:
        return "key needed"


def delete_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        response = delete(request.headers["key"],request.form['queue_name'])
        print(response.code)
        return "delete queue"
    else:
        return "key needed"

def list_queues(request):
    if 'key' in request.headers:
        response = list(request.headers["key"])
        print(response.code)
        print(response.queues)
        return "list queues"
    else:
        return "key needed"


def subscribe_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        response = subscribe(request.headers["key"],request.form['queue_name'])
        print(response.code)
        return "Subscribe queue"
    else:
        return "key needed"


def publish_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        print(request.form['message'])
        response = publish(request.headers["key"],request.form['queue_name'],request.form['message'])
        print(response.code)
        return "publish queue"
    else:
        return "key needed"


def consume_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        response = consume(request.headers["key"],request.form['queue_name'])
        print(response.code)
        print(response.message)
        return "Consume queue"
    else:
        return "key needed"