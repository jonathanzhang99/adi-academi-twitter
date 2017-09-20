from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from flask_moment import Moment

import os


login_manager = LoginManager()
login_manager.session_protection = 'string'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = MongoEngine()
mail = Mail()
moment = Moment()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

    app.config['MAIL_HEADER'] = '[AcademiTwitter]'

    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
