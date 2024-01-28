from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Create instances of SQLAlchemy and Bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User model representing a registered user."""
    
    __tablename__='users'
    
    # User model columns
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), primary_key=True, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def fullname(self):
        """Returns the full name of the user."""
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def register(cls, first_name, last_name, username, email, password):
        """Register a new user and hash the password."""
        hash_utf8 = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hash_utf8
        )

    @classmethod
    def authorize(cls, username, password):
        """Authenticate a user by checking the username and password."""
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

class Feedback(db.Model):
    """Feedback model representing user feedback."""
    
    __tablename__='feedback'
    
    # Feedback model columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, db.ForeignKey('users.username'))
    
    # Relationship to the User model
    user = db.relationship('User', backref='feedbacks')
