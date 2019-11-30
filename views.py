from flask import Flask
from authform import LoginForm,RegisterForm
#  flask_login import login_required,current_user
from flask import render_template,url_for,flash,redirect
#  ,request,redirect,url_for,abort
# from ..models import User,Comment,Pitch,Example
# from ..import db,photos
# from .forms import UpdateProfile,UpdatePitch,CommentForm
# from . import main
# import markdown2
app = Flask(__name__)
app.config['SECRET_KEY']='924aa84d9830e3138f9caeb669c646dd'
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
@app.route("/register", methods=['GET','POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    flash (f'An account has been created for {form.username.data}','Success')
    return redirect (url_for('index'))

  return render_template('register.html', title='Register',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data =="perry" and form.password.data =="qwerty":
      flash (f'Welcome {form.username.data}','Success')
      return redirect (url_for('index'))
  else:
    flash('Login Usuccessful. Please confirm your credentials','danger')

    return redirect (url_for('login'))


    

  return render_template('login.html', title='Login',form = form)


if __name__ == '__main__':
    app.run(debug=True)


