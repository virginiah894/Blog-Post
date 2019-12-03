from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  id =db.Column(db.Integer,primary_key= True)
  email =db.Column(db.String(100),unique= True,nullable= False)
  username =db.Column(db.String(100),unique= True,nullable= False)
  image_file =db.Column(db.String(100),nullable= False, default="default.jpeg")
  password =db.Column(db.String(100),nullable= False)
  posts =db.relationship('Post',backref= 'author',lazy=True)
  def __repr__(self):
    return f"User('{self.email}','{self.username}','{self.image_file}')"

class Post(db.Model):
  id =db.Column(db.Integer,primary_key= True)
  title =db.Column(db.String(100),nullable= False)
  date_posted =db.Column(db.DateTime,nullable= False,default=datetime.utcnow)
  content =db.Column(db.Text,nullable= False)
  user_id= db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  def __repr__(self):
    return f"Post('{self.title}','{self.date_posted}')"

class Quote:

  def __init__ (self,author,quote,permalink):

    self.author = author
    self.quote = quote
    self.permalink = permalink
    

