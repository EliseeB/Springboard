"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


default_url_image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Windows_10_Default_Profile_Picture.svg/2048px-Windows_10_Default_Profile_Picture.svg.png'


class User(db.Model):
    """User"""

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(35), nullable=False)

    last_name = db.Column(db.String(35), nullable=False)

    image_url = db.Column(db.String(300), nullable=False, default=default_url_image)


def connect_db(app):
    """Connects to database"""
    db.app = app

    db.init_app(app)
    