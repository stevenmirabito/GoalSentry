"""
Goal Sentry API
User Authentication Module
"""

import requests


class Authentication:
    def __init__(self):
        pass

    @staticmethod
    def user_from_identifier(identifier):
        user = requests.get('http://www.csh.rit.edu:56124/?ibutton=' + identifier).json()

        if "error" in user:
            raise ValueError("Unable to retrieve user: " + user["error"])
        else:
            return {
                "username": user["uid"],
                "name": user["cn"],
                "email": user["uid"] + '@csh.rit.edu'
            }
