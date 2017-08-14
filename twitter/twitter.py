from flask import Flask, render_template, session, url_for, redirect
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from mongoengine import *
from models import LoginForm

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "sungbyflamingtonguesabove"

login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap()
bootstrap.init_app(app)

db = MongoEngine()
db.init_app(app)


@app.route('/', methods=["GET", "POST"])
def home_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            user.save()
            session['known'] = False
        else:
            session['known'] = True
        session['username'] = form.username.data
        form.username.data = ''
        return redirect(url_for('home_page'))
    return render_template('home.html', name=session.get('username'), form=form, known=session.get('known', False))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class User(db.Document):
    username = StringField(required=True, unique=True)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Post(db.Document):
    author = ReferenceField(User, reverse_delete_rule=CASCADE)

if __name__ == '__main__':
    app.run()
