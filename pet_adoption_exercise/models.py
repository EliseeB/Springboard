from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


default_pet_image = 'https://posfacturar.com/pos_organicnails/public/upload/default_image/default_pet.jpg'


class Pet(db.Model):
    
    __tablename__='pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, nullable=True, default=default_pet_image)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=False)

    available = db.Column(db.Boolean, nullable=False, default=True)




