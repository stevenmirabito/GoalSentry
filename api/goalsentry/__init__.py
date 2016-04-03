"""
Goal Sentry API
Main Application
"""

from flask import Flask, request
from database import session as db
from json import dumps as jsonify
from utilities import row2dict
import authentication
import models

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Goal Sentry API</h1>"


"""
Standard Return Format Helpers
"""


def return_user(user):
    user_dict = row2dict(user)
    scores_list = []

    scores = models.Score.query.filter_by(user_id=user.id)
    for score in scores:
        scores_list.append(row2dict(score))

    user_dict["scores"] = scores_list
    return user_dict


def return_game(game):
    game_dict = row2dict(game)
    game_dict["completed"] = (not not game.time_completed)

    scores_list = []
    for score in game_dict.scores:
        scores_list.append(row2dict(score))

    return game_dict


def return_table(table):
    table_dict = row2dict(table)
    last_game = models.Game.query.filter_by(table_id=table.id).order_by(models.Game.time_started.desc()).first()

    if not last_game.time_completed:
        # Game is still in progress
        table_dict["in_use"] = True
        table_dict["game"] = row2dict(last_game)
    else:
        table_dict["in_use"] = False

    return table_dict


def return_success():
    return {
        "status": {
            "success": True
        }
    }


def return_error(e):
    return {
        "status": {
            "success": False,
            "message": e.message
        }
    }


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
        response = return_user(user)
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


@app.route("/users", methods=["POST"])
def register_user(user_data=request.get_json(force=True)["user"]):
    try:
        user = models.User(username=user_data["username"], name=user_data["name"], email=user_data["email"])
        db.add(user)
        db.commit()
        response = return_success()
    except Exception as e:
        response = return_error(e)

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
        response = return_error(e)

    return jsonify(response)


@app.route("/games", methods=["POST"])
def new_game():
    data = request.get_json(force=True)
    try:
        game = models.Game(table_id=data["game"]["table_id"])
        db.add(game)
        db.commit()
        response = return_success()
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


@app.route("/game/<game_id>/authenticate", methods=["POST"])
def authenticate_to_game(game_id):
    data = request.get_json(force=True)
    try:
        auth = authentication.Authentication()
        user_data = auth.user_from_identifier(data["authenticate"]["identifier"])
        users = models.User.query.filter_by(username=user_data["username"])

        if users.length > 0:
            # User is already registered
            user_id = users.first().id
        else:
            # User is not registered, register them
            register_user(user_data=user_data)
            user_id = models.User.query.filter_by(username=user_data["username"]).first().id

        game = models.Game.query.filter_by(id=game_id).first()
        score = models.Score(user_id=user_id, game_id=game.id)
        db.add(score)
        db.commit()

        response = return_success()
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


@app.route("/game/<game_id>", methods=["DELETE"])
def delete_game(game_id):
    try:
        game = models.Game.query.filter_by(id=game_id).first()
        db.delete(game)

        for score in models.Score.query.filter_by(game_id=game_id):
            db.delete(score)

        db.commit()

        response = {
            "status": {
                "success": True
            }
        }
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


"""
Table Routes
"""


@app.route("/tables", methods=["GET"])
def get_all_tables():
    tables = []
    for table in models.Table.query.all():
        tables.append(return_table(table))

    return jsonify(tables)


@app.route("/tables", methods=["POST"])
def new_table():
    data = request.get_json(force=True)
    try:
        table = models.Table(name=data["table"]["name"])
        db.add(table)
        db.commit()
        response = return_success()
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


@app.route("/table/<table_id>", methods=["GET"])
def get_table_by_id(table_id):
    try:
        table = models.Table.query.filter_by(id=table_id).first()
        response = return_table(table)
    except Exception as e:
        response = return_error(e)

    return jsonify(response)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
