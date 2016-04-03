from flask import Flask, request
from database import session as db

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>Goal Sentry API</h1>"