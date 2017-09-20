from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Enter a username")])
    email = StringField('Email', validators=[InputRequired(message='Enter an email'), Email('Invalid email')])
    password = PasswordField('Password')
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    text = TextAreaField('Let the world know your thoughts!',
                         validators=[InputRequired(message='Please write something!'),
                                     Length(1, 140, message='No more than 140 characters allowed')])
    submit = SubmitField('Submit')
