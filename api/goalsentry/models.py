"""
Goal Sentry API
Models
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from datetime import datetime as dt
from sqlalchemy.orm import relationship
from database import Base

user_game_mapper = Table('user_game_rel', Base.metadata, Column('user_id', Integer, ForeignKey('users.id')),
                         Column('game_id', Integer, ForeignKey('games.id')))


class User(Base):
    __tablename__ = 'users'

    # Basic metadata
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    name = Column(String(120))
    email = Column(String(120))
    rank = Column(Integer)

    # Create a many-to-many relationship with Game
    games = relationship("Game", secondary=user_game_mapper, back_populates="users")

    def __init__(self, username=None, name=None, email=None):
        self.username = username
        self.name = name
        self.email = email.lower()
        self.rank = 0

    def __repr__(self):
        return '<Student %r>' % self.username


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

    # Create a many-to-many relationship with User
    users = relationship("User", secondary=user_game_mapper, back_populates="games")

    # Create a many-to-one relationship with Table
    table_id = Column(Integer, ForeignKey('tables.id'))

    def __init__(self, time_started=None):
        if time_started:
            # Convert dates to ISO 8601
            self.time_started = dt.strptime(time_started, "%Y-%m-%d %H:%M:%S.%f")
        else:
            # Store the current time
            self.time_started = dt.now()

        self.time_completed = None

    def __repr__(self):
        return '<Game %r>' % self.id
