from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,Required
from app.models import User, Post

class RegisterForm(FlaskForm):
  email= StringField('Your Email Address',validators=[DataRequired(),Email()])
  username = StringField('Enter your username',validators = [DataRequired(),Length(min=2,max=10)])
  
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('confirm_password',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm your  Password ',validators = [Required()])
  submit = SubmitField('Sign Up')
  # ensure no multiple accoutns with similar credentials
  def validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('An account with that email exists.Please use another one')
  
  def validate_username(self,username):
    user = User .query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('An account with that username exists,please choose another username')

class LoginForm(FlaskForm):
  username = StringField('Enter your username',validators=[Required()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login In')
class BlogForm(FlaskForm):
  title = StringField('Title',validators=[Required()])
  content = TextAreaField('Content',validators=[Required()])
  submit = SubmitField('Submit')