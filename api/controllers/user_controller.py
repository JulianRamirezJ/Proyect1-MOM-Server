from flask import Flask, render_template, request, redirect
from methods.user import *
def create_user():
    response = create()
    if response.code == 200:
        return "Your key is {}".format(response.key)
    return "Request returned error code{}".format(response.code)
