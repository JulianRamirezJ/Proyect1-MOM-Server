from flask import Flask, render_template, request, redirect
from controllers import topic_controller
from controllers import queue_controller
from controllers import user_controller

def register(app):
    #user
    @app.route('/create_user', methods=["GET"])
    def create_user():
        return user_controller.create_user()

    #Topics
    @app.route('/create_topic', methods=["POST"])
    def create_topic():
        return topic_controller.create_topic(request)

    @app.route('/delete_topic', methods=["POST"])
    def delete_topic():
        return topic_controller.delete_topic(request)

    @app.route('/list_topics', methods=["POST"])
    def list_topics():
        return topic_controller.list_topics(request)
    
    @app.route('/subscribe_topic', methods=["POST"])
    def subscribe_topic():
        return topic_controller.subscribe_topic(request)

    @app.route('/publish_topic', methods=["POST"])
    def publish_topic():
        return topic_controller.publish_topic(request)

    @app.route('/consume_topic', methods=["POST"])
    def consume_topic():
        return topic_controller.consume_topic(request)

    #Queues
    @app.route('/create_queue', methods=["POST"])
    def create_queue():
        return queue_controller.create_queue(request)

    @app.route('/delete_queue', methods=["POST"])
    def delete_queue():
        return queue_controller.delete_queue(request)

    @app.route('/list_queues', methods=["POST"])
    def list_queues():
        return queue_controller.list_queues(request)

    @app.route('/subscribe_queue', methods=["POST"])
    def subscribe_queue():
        return queue_controller.subscribe_queue(request)

    @app.route('/publish_queue', methods=["POST"])
    def publish_queue():
        return queue_controller.publish_queue(request)

    @app.route('/consume_queue', methods=["POST"])
    def consume_queue():
        return queue_controller.consume_queue(request)