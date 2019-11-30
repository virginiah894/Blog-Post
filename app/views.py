from flask import render_template,url_for,flash,redirect
from app.authform import LoginForm,RegisterForm
from app.models import User,Post
from app import app


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

    flash (f'An account has been created for {form.username.data}', 'success')
    return redirect (url_for('index'))

  return render_template('register.html', title='Register',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data =="perry" and form.password.data =="qwerty":
      flash (f'Welcome {form.username.data}','success')
      return redirect (url_for('index'))
    else:
      flash('Login Usuccessful. Please confirm your credentials','danger')

  return render_template('login.html', title='Login',form = form)




