"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


default_url_image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Windows_10_Default_Profile_Picture.svg/2048px-Windows_10_Default_Profile_Picture.svg.png'


class User(db.Model):
    """User"""

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(35), nullable=False)

    last_name = db.Column(db.String(35), nullable=False)

    image_url = db.Column(db.String(300), nullable=False, default=default_url_image)



class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")




def connect_db(app):
    """Connects to database"""
    db.app = app

    db.init_app(app)
    