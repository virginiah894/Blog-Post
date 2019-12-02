import os
import secrets
from PIL import Image
from flask import url_for,current_app
from flask_mail import Message
from app import mail


def save_pp(form_pic):
  random_data = secrets.token_hex(10)
  _,f_ext = os.path.splitext(form_pic.filename)
  picture_filename = random_data + f_ext
  image_path = os.path.join(current_app.root_path,'static/profile_pics',picture_filename)
  # resize the image
  output_size =(166,166)
  newImage = Image.open(form_pic)
  newImage.thumbnail(output_size)
  newImage.save(image_path)
  return  picture_filename
