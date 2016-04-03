from flask import Flask
from database import session as db

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:red'>Goal Sentry API</h1>"


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
