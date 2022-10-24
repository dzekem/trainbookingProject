from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_flask_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\xe6=;\x16E\x03\xe5\x1d\xc0\xd3\xfa}\x17V\xa8\x9a\xa4\xe6\x02~\xa4\xd2\r\x0c'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
