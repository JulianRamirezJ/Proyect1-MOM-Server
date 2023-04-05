from flask import Flask, render_template, request, redirect


def create_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        return "create queue"
    else:
        return "key needed"


def delete_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        return "delete queue"
    else:
        return "key needed"

def list_queues(request):
    if 'key' in request.headers:
        return "list queues"
    else:
        return "key needed"


def subscribe_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        return "Subscribe queue"
    else:
        return "key needed"


def publish_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        print(request.form['message'])
        return "publish queue"
    else:
        return "key needed"


def consume_queue(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['queue_name'])
        return "Consume queue"
    else:
        return "key needed"