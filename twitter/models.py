from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class User():
    pass


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Enter a username")])
    password = PasswordField('Password')
    submit = SubmitField('Submit')
