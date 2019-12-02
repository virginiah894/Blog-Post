from flask import Blueprint
from flask import render_template,url_for,flash,redirect,request,abort
# from app.authform import LoginForm,RegisterForm,BlogForm,UpdateProfileForm
from app.models import Post
from app.posts.forms import BlogForm
from app import db
from flask_login import current_user,login_required





posts = Blueprint('posts',__name__)

@posts.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
  form = BlogForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data,content=form.content.data,author=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your new  blog post has been created!','success')
    return redirect(url_for('main.index'))
    
  return render_template("NewBlog.html",title= "New Blog",form=form,legend='New Blog')

# displaying the posts created
@posts.route('/blog/<int:post_id>')
# @login_required
def blog(post_id):
  post =Post.query.get_or_404(post_id)
  return render_template('blog.html',title= post.title,post=post)

# updating blogs
@posts.route('/blog/<int:post_id>/update',methods=['GET','POST'])
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
    return redirect(url_for('posts.blog',post_id=post.id))
  elif request.method =='GET':
    form.title.data=post.title
    form.content.data=post.content
  return render_template("NewBlog.html",title= "Update Blog",form=form,legend='Update Blog')


@posts.route('/blog/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_blog(post_id):
  post =Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your blog has been deleted','danger')
  return redirect(url_for('main.index'))
