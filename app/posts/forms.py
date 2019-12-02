
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Required



class BlogForm(FlaskForm):
  title = StringField('Title',validators=[Required()])
  content = TextAreaField('Content',validators=[Required()])
  submit = SubmitField('Submit')
