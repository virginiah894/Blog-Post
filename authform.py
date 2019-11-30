from flask_wtf import FlaskForm
from wtforms import StringField.PasswordFieldB
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,BooleanField

class RegisterForm(FlaskForm):
  email= StringField('Your Email Address',validators=[DataRequired(),Email()])
  username = StringField('Enter your username',validators = [DataRequired(),Length(min=2,max=10)])
  
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm Passwords',validators = [Required()])
  submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
  email = StringField('Your Email Address',validators=[Required(),Email()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login In')