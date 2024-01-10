from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, SelectField, URLField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding a new pet for adoption"""
    
    name = StringField('Name', validators=[ InputRequired(), Length(min=1, max=50)])

    species = SelectField('Species', choices=[ ('cat','Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine') ], validators=[ InputRequired() ] )
    
    photo_url = URLField('Url Photo', validators=[Optional(), URL()])

    age = IntegerField('How hold is the pet?', validators=[Optional(), NumberRange(min=0, max=30)] )

    note = StringField('Notes', validators=[Optional()])

    available = RadioField('Is the pet available?', choices=[ (True, 'Available'), (False, 'Unavailable') ], validators=[InputRequired()])

