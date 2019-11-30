from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,Required

class RegisterForm(FlaskForm):
  email= StringField('Your Email Address',validators=[DataRequired(),Email()])
  username = StringField('Enter your username',validators = [DataRequired(),Length(min=2,max=10)])
  
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('confirm_password',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm your  Password ',validators = [Required()])
  submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
  username = StringField('Enter your username',validators=[Required()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login In')
  