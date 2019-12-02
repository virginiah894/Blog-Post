import secrets
import os
from flask import render_template,url_for,flash,redirect,request,abort
from app.authform import LoginForm,RegisterForm,BlogForm,UpdateProfileForm
from app.models import User,Post
from app import app,db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required


# posts = [
# {
#   'author': 'Otto Von Mccery',
#   'title': 'Purpink Cherry',
#   'category': 'Health and Wellness',
#   'content': 'Let us talk mental health',
#   'posted_on': 'November 30,2019',
# },
# {
#     'author': 'Ethan Lawinsky',
#   'title': 'Over Twenty Five',
#   'category': 'Lifestyle',
#   'content': 'A visit to the dentist was awesome',
#   'posted_on': 'November 30,2019',

# }
# ]

@app.route('/')

def index():
  posts=Post.query.all()


  return render_template('index.html',posts = posts )
@app.route("/about")
def about():
    

    return render_template('about.html', title='About')
@app.route("/register", methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegisterForm()
  if form.validate_on_submit():

    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(email=form.email.data,username=form.username.data,password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash (f'An account has been created for {form.username.data}.You can now Log in', 'success')
    return redirect (url_for('login'))

  return render_template('register.html', title='Register',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password,form.password.data):
      login_user(user,remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('profile'))
      flash (f'Welcome {form.username.data}','success')
      return redirect (url_for('index'))

    else:
      flash('Login Usuccessful. Please confirm your credentials','danger')

  return render_template('login.html', title='Login',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))



def save_pp(form_pic):
  random_data = secrets.token_hex(10)
  _,f_ext = os.path.splitext(form_pic.filename)
  picture_filename = random_data + f_ext
  image_path = os.path.join (app.root_path,'static/profile_pics',picture_filename)
  form_pic.save(image_path)
  return  picture_filename


@app.route('/profile',methods=['GET','POST'])
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
    return redirect (url_for('profile'))
  elif request.method == 'GET':
    form.email.data= current_user.email
    form.username.data= current_user.username




  image_file = url_for('static',filename='profile_pics/'+ current_user.image_file)
  return render_template("profile.html",title ="profile",image_file=image_file,form=form)
  

  # create a post
@app.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
  form = BlogForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data,content=form.content.data,author=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your new  blog post has been created!','success')
    return redirect(url_for('index'))
    
  return render_template("NewBlog.html",title= "New Blog",form=form,legend='New Blog')

# displaying the posts created
@app.route('/blog/<int:post_id>')
# @login_required
def blog(post_id):
  post =Post.query.get_or_404(post_id)
  return render_template('blog.html',title= post.title,post=post)

# updating blogs
@app.route('/blog/<int:post_id>/update',methods=['GET','POST'])
@login_required
def blog_update(post_id):
  post =Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  form=BlogForm()
  if form.validate_on_submit():
    post.title= form.title.data
    post.content= form.content.data
    db.session.commit()
    flash('Update successful','success')
    return redirect(url_for('blog',post_id=post.id))
  elif request.method =='GET':
    form.title.data=post.title
    form.content.data=post.content
  return render_template("NewBlog.html",title= "Update Blog",form=form,legend='Update Blog')


@app.route('/blog/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_blog(post_id):
  post =Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your blog has been deleted','danger')
  return redirect(url_for('index'))
