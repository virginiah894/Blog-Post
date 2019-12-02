from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'userauth.login'
login_manager.login_message_category = 'danger'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.userauth.views import userauth
    from app.posts.views import posts
    from app.main.views import main
    app.register_blueprint(userauth)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app