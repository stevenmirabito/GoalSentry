"""
Goal Sentry API
Models
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime as dt
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'

    # Basic metadata
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    name = Column(String(120))
    email = Column(String(120))
    rank = Column(Integer)

    # Create a one-to-many relationship with Score
    scores = relationship("Score")

    def __init__(self, username=None, name=None, email=None):
        self.username = username
        self.name = name
        self.email = email.lower()
        self.rank = 0

    def __repr__(self):
        return '<User %r>' % self.username


class Table(Base):
    __tablename__ = 'tables'

    # Basic metadata
    id = Column(Integer, primary_key=True)
    name = Column(String(120))

    # Create a one-to-many relationship with Game
    games = relationship("Game")

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Table %r>' % self.id


class Game(Base):
    __tablename__ = 'games'

    # Basic metadata
    id = Column(Integer, primary_key=True)
    time_started = Column(DateTime)
    time_completed = Column(DateTime)

    # Create a one-to-many relationship with Score
    scores = relationship("Score")

    # Create a many-to-one relationship with Table
    table_id = Column(Integer, ForeignKey('tables.id'))

    def __init__(self, time_started=None, table_id=None):
        if time_started:
            # Convert dates to ISO 8601
            self.time_started = dt.strptime(time_started, "%Y-%m-%d %H:%M:%S.%f")
        else:
            # Store the current time
            self.time_started = dt.now()

        self.time_completed = None

        if table_id:
            self.table_id = table_id

    def __repr__(self):
        return '<Game %r>' % self.id


class Score(Base):
    __tablename__ = 'scores'

    # Basic metadata
    id = Column(Integer, primary_key=True)
    score = Column(Integer)

    # Create a one-to-many relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))

    # Create a one-to-many relationship with Game
    game_id = Column(Integer, ForeignKey('games.id'))

    def __init__(self, score=0, user_id=None, game_id=None):
        self.score = score
        if user_id:
            self.user_id = user_id

        if game_id:
            self.game_id = game_id

    def __repr__(self):
        return '<Score %r>' % self.id
