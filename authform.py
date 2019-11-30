from flask_wtf import FlaskForm
from wtforms import StringField.PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

class RegisterForm(FlaskForm):
  email= StringField('Your Email Address',validators=[DataRequired(),Email()])
  username = StringField('Enter your username',validators = [DataRequired(),Length(min=2,max=10)])
  password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
  password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
  
  submit = SubmitField('Sign Up')
