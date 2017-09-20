from mongoengine import StringField, EmailField, DateTimeField, ReferenceField, ListField, CASCADE
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


class User(db.Document, UserMixin):
    username = StringField(required=True, unique=True)
    password_hash = StringField(max_length=128, required=True)
    email = EmailField(max_length=128, required=True)

    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Comment(db.Document):
    text = StringField(required=True, max_length=100)
    timestamp = DateTimeField(required=True, default=datetime.now())
    author = ReferenceField(User, reverse_delete_rule=CASCADE)


class Post(db.Document):
    body = StringField(required=True, max_length=140)
    timestamp = DateTimeField(required=True, default=datetime.utcnow())
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    comments = ListField(ReferenceField(Comment))
