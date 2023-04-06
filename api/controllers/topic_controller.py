from flask import Flask, render_template, request, redirect
from methods.topic import *
def create_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        response = create(request.headers["key"],request.form['topic_name'])
        print(response.code)
        return "create topic"
    else:
        return "key needed"

def delete_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        response = delete(request.headers["key"],request.form['topic_name'])
        print(response.code)
        return "delete topic"
    else:
        return "key needed"


def list_topics(request):
    if 'key' in request.headers:
        response = list(request.headers["key"])
        print(response.code)
        print(response.topics)
        return "list topics"
    else:
        return "key needed"


def subscribe_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        response = subscribe(request.headers["key"],request.form['topic_name'])
        print(response.code)
        return "subscribe topic"
    else:
        return "key needed"


def publish_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        print(request.form['message'])
        response = publish(request.headers["key"],request.form['topic_name'], request.form['message'])
        print(response.code)
        return "publish topic"
    else:
        return "key needed"


def consume_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        response = consume(request.headers["key"],request.form['topic_name'])
        print(response.code)
        print(response.message)
        return "consume topic"
    else:
        return "key needed"