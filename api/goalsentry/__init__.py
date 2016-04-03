"""
Goal Sentry API
Main Application
"""

from flask import Flask, request
from database import session as db
from json import dumps as jsonify
from utilities import row2dict
import models

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Goal Sentry API</h1>"


"""
User Routes
"""


@app.route("/users", methods=["GET"])
def get_all_users():
    users = []
    for user in models.User.query.all():
        user_dict = row2dict(user)
        users.append(user_dict)

    return jsonify(users)


@app.route("/user/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    try:
        user = models.User.query.filter_by(id=user_id).first()
        response = row2dict(user)
    except Exception as e:
        response = dict()
        response[0]["status"]["success"] = False
        response[0]["status"]["message"] = e.message

    return jsonify(response)


"""
Game Routes
"""


@app.route("/games", methods=["GET"])
def get_all_games():
    games = []
    for game in models.Game.query.all():
        game_dict = row2dict(game)
        games.append(game_dict)

    return jsonify(games)


@app.route("/game/<game_id>", methods=["GET"])
def get_game_by_id(game_id):
    try:
        game = models.Game.query.filter_by(id=game_id).first()
        response = row2dict(game)
    except Exception as e:
        response = dict()
        response[0]["status"]["success"] = False
        response[0]["status"]["message"] = e.message

    return jsonify(response)


@app.route("/games", methods=["POST"])
def new_game():
    data = request.get_json(force=True)
    try:
        game = models.Game()
        db.add(game)
        db.commit()
        response = row2dict(game)
    except Exception as e:
        response = dict()
        response[0]["status"]["success"] = False
        response[0]["status"]["message"] = e.message

    return jsonify(response)


@app.route("/game/<id>/authenticate", methods=["POST"])
def authenticate_to_game(id):
    pass


@app.route("/game/<game_id>", methods=["DELETE"])
def delete_game(game_id):
    data = request.get_json(force=True)
    response = dict()
    try:
        game = models.Game.query.filter_by(id=game_id).first()
        db.delete(game)
        db.commit()
        response[0]["status"]["success"] = True
    except Exception as e:
        response[0]["status"]["success"] = False
        response[0]["status"]["message"] = e.message

    return jsonify(response)


"""
Table Routes
"""


@app.route("/table/<table_id>", methods=["GET"])
def get_table_by_id(table_id):
    try:
        table = models.Table.query.filber_by(id=table_id).first()
        response = row2dict(table)
    except Exception as e:
        response = dict()
        response[0]["status"]["success"] = False
        response[0]["status"]["message"] = e.message

    return jsonify(response)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
