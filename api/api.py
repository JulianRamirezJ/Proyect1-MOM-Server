from flask import Flask, render_template, request, redirect
from routes import register
#Setup our app
app = Flask(__name__)

register(app)

if __name__ == "__main__":
    app.run()