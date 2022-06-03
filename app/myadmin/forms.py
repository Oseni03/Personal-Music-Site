from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from app.models import Type
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, FileField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
  
  
class LoginForm(FlaskForm):
  username = StringField("Username",
          validators=[DataRequired()])
  password = PasswordField("Password", 
            validators=[DataRequired()])
  submit = SubmitField("Login")
  