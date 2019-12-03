from flask import render_template,url_for,flash,redirect, request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db,bcrypt
from app.models import User,Post
from app.userauth.forms import RegisterForm, LoginForm, UpdateProfileForm
from app.userauth.utilities import save_pp
from ..email import mail_message




from flask import Blueprint

userauth = Blueprint('userauth',__name__)


@userauth.route("/register", methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegisterForm()
  if form.validate_on_submit():

    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(email=form.email.data,username=form.username.data,password=hashed_password)
    db.session.add(user)
    db.session.commit()
    mail_message("Welcome to Blogs World","email/welcome_user",user.email,user=user)

    flash (f'An account has been created for {form.username.data}.You can now Log in', 'success')
    return redirect (url_for('userauth.login'))

  return render_template('register.html', title='Register',form = form)

@userauth.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password,form.password.data):
      login_user(user,remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.index'))
      flash (f'Welcome {form.username.data}','success')
      return redirect (url_for('userauth.profile'))

    else:
      flash('Login Usuccessful. Please confirm your credentials','danger')

  return render_template('login.html', title='Login',form = form)

@userauth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@userauth.route('/profile',methods=['GET','POST'])
@login_required
def profile():
  form =UpdateProfileForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file = save_pp(form.picture.data)
      current_user.image_file = picture_file
    current_user.email = form.email.data
    current_user.username = form.username.data
    db.session.commit()
    flash('Profile Update Successful','primary')
    return redirect (url_for('userauth.profile'))
  elif request.method == 'GET':
    form.email.data= current_user.email
    form.username.data= current_user.username




  image_file = url_for('static',filename='profile_pics/'+ current_user.image_file)
  return render_template("profile.html",title ="profile",image_file=image_file,form=form)
  

  

