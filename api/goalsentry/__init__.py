from flask import Flask
from database import session as db

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:red'>Goal Sentry API</h1>"


"""
User Routes
"""


@app.route("/users", methods=["GET"])
def get_all_users():
    pass


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    pass


"""
Game Routes
"""


@app.route("/games", methods=["GET"])
def get_all_games():
    pass


@app.route("/game/<id>", methods=["GET"])
def get_game_by_id(id):
    pass


@app.route("/games", methods=["POST"])
def new_game():
    pass


@app.route("/game/<id>/authenticate", methods=["POST"])
def authenticate_to_game(id):
    pass


@app.route("/game/<id>", methods=["DELETE"])
def delete_game(id):
    pass


"""
Table Routes
"""


@app.route("/table/<id>", methods=["GET"])
def get_table_by_id(id):
    pass


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
