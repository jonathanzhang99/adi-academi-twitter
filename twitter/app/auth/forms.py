from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import InputRequired, Email, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Enter email'), Email('Invalid email')])
    password = PasswordField('Password', validators=[InputRequired('Enter a password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Enter email'), Email('Invalid email')])
    username = StringField('Username', validators=[InputRequired('Enter username'),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, "Username can only contain "
                                                                                         "letters, numbers, underscores"
                                                                                         " or periods")
                                                   ])
    password = PasswordField('Password', validators=[InputRequired('Enter password'),
                                                     EqualTo('password2', 'Passwords must match'),
                                                     Length(1, 128)
                                                     ])
    password2 = PasswordField('Confirm Password', validators=[InputRequired('Confirm password')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.objects(email=field.data).first() != None:
            raise ValidationError("Email already taken")

    def validate_username(self, field):
        if User.objects(username=field.data).first() != None:
            raise ValidationError("Username already taken")