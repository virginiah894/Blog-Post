from flask import Flask
#  flask_login import login_required,current_user
from flask import render_template,url_for
#  ,request,redirect,url_for,abort
# from ..models import User,Comment,Pitch,Example
# from ..import db,photos
# from .forms import UpdateProfile,UpdatePitch,CommentForm
# from . import main
# import markdown2
app = Flask(__name__)
posts = [
{
  'author': 'Virginiah Periah',
  'title': 'Purpink Cherry',
  'category': 'Health and Wellness',
  'content': 'Let us talk mental health',
  'posted_on': 'November 30,2019',
},
{
    'author': 'Ethan Lawinsky',
  'title': 'Over Twenty Five',
  'category': 'Lifestyle',
  'content': 'A visit to the dentist was awesome',
  'posted_on': 'November 30,2019',

}
]

@app.route('/')

def index():


    return render_template('index.html',posts = posts )
@app.route("/about")
def about():
    

    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)


