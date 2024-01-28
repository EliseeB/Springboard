from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length


class RegistrationForm(FlaskForm):
    
    first_name = StringField('First name', validators=[InputRequired(), Length(min=3, max=30)])
    
    last_name = StringField('Last name', validators=[InputRequired(), Length(min=3, max=30)])
    
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)])
    
    email = EmailField('Email', validators=[InputRequired(), Length(max=50)])
    
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3)])
    



class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[InputRequired()])
    
    password = PasswordField('Password', validators=[InputRequired()])
    
    
    

class FeedbackForm(FlaskForm):
    
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    
    content = TextAreaField('Content', validators=[InputRequired()])
    

class UpdateFeedback(FlaskForm):
    
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    
    content = TextAreaField('Content', validators=[InputRequired()])
    
  