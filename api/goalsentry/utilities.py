"""
Goal Sentry API
Utility Functions
"""


def row2dict(row):
    """
    Converts a SQLAlchemy ORM row to a dictionary
    Thanks to Anurag Uniyal: http://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    :param row: Row object to convert
    :return: Dictionary representation of the row object
    """

    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
