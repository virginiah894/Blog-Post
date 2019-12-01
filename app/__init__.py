from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# flask_login import login_required,current_user
#  ,request,redirect,url_for,abort

# from ..import db,photos
# from .forms import UpdateProfile,UpdatePitch,CommentForm
# from . import main
# import markdown2


app = Flask(__name__)
app.config['SECRET_KEY']='924aa84d9830e3138f9caeb669c646dd'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt= Bcrypt()
login_manager = LoginManager(app)
from app import views
