from flask import Blueprint , render_template, request
from app.models import Post


main = Blueprint('main',__name__)

@main.route('/')
def index():
  posts=Post.query.all()


  return render_template('index.html',posts = posts )
@main.route("/about")
def about():
    

    return render_template('about.html', title='About')

