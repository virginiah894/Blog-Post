from flask import Blueprint , render_template, request
from app.models import Post
from app.request import display_quote


main = Blueprint('main',__name__)

@main.route('/')
def index():
  posts=Post.query.all()
  quote =display_quote()


  return render_template('index.html',posts = posts,quote=quote )
@main.route("/about")
def about():
  quote =display_quote()
  return render_template('about.html', title='About',quote=quote)

