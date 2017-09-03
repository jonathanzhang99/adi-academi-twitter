from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine

import os

login_manager = LoginManager()
login_manager.session_protection = 'string'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or 'hasdoifhaoidfhsd'
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app