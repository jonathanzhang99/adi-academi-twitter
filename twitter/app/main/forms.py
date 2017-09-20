from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Enter a username")])
    email = StringField('Email', validators=[InputRequired(message='Enter an email'), Email('Invalid email')])
    password = PasswordField('Password')
    submit = SubmitField('Submit')