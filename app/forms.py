from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired


#Exercise 5
class UploadForm(FlaskForm):
    file = FileField('Image File', 
                     validators=[
                         FileRequired(),  
                         FileAllowed(['jpg', 'png'], 'Images only!')  
                     ])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])








