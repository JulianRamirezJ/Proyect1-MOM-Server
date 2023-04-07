from flask import Flask, render_template, request, redirect
from methods.topic import *
def create_topic(request):
    if 'key' in request.headers and 'topic_name' in request.form:
        response = create(request.headers["key"],request.form['topic_name'])
        if response.code == 200:
            return "Topic created sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the topic_name"

def delete_topic(request):
    if 'key' in request.headers and 'topic_name' in request.form:
        response = delete(request.headers["key"],request.form['topic_name'])
        if response.code == 200:
            return "Topic deleted sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the topic_name"


def list_topics(request):
    if 'key' in request.headers:
        response = list(request.headers["key"])
        if response.code == 200:
            return "Your topics are {}".format(response.topics)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key "


def subscribe_topic(request):
    if 'key' in request.headers and 'topic_name' in request.form:
        response = subscribe(request.headers["key"],request.form['topic_name'])
        if response.code == 200:
            return "Subcribed to topic sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the topic_name"


def publish_topic(request):
    if 'key' in request.headers and 'topic_name' in request.form:
        response = publish(request.headers["key"],request.form['topic_name'], request.form['message'])
        if response.code == 200:
            return "Published to topic sucesfully {}".format(response.code)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the topic_name"


def consume_topic(request):
    if 'key' in request.headers and 'topic_name' in request.form:
        response = consume(request.headers["key"],request.form['topic_name'])
        if response.code == 200:
            return "consumed from topic, message: {}".format(response.message)
        return "Request returned error code {}".format(response.code)
    else:
        return "Make sure you added your key and the topic_name"