from flask import Flask, render_template, request, redirect

def create_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        return "create topic"
    else:
        return "key needed"

def delete_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        return "delete topic"
    else:
        return "key needed"


def list_topics(request):
    if 'key' in request.headers:
        return "list topics"
    else:
        return "key needed"


def subscribe_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        return "subscribe topic"
    else:
        return "key needed"


def publish_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        print(request.form['message'])
        return "publish topic"
    else:
        return "key needed"


def consume_topic(request):
    if 'key' in request.headers:
        print(request.headers["key"])
        print(request.form['topic_name'])
        return "consume topic"
    else:
        return "key needed"