from flask import Flask, render_template, request, redirect
import config
#Setup our app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST)