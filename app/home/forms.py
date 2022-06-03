from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask import current_app 
from app import create_app
from app.models import Type
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, FileField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
app = create_app()

  
with app.app_context():
  types = Type.query.order_by(Type.id).all()
  
class AlbumForm(FlaskForm):
  title = StringField("Album Title", validators=[DataRequired()])
  picture = FileField("Update profile picture", validators=[FileAllowed(["jpg", "png"])])
  submit = SubmitField("Create Album")
  
class TrackForm(FlaskForm):
  title = StringField("Track Title", validators=[DataRequired()])
  song = FileField("Add song", validators=[DataRequired()])
  genre = SelectField("Type/Genre", choices=[(gen.id, gen.name) for gen in types])
  submit = SubmitField("Add Track")
  
class SinglesForm(FlaskForm):
  title = StringField("Single Title", validators=[DataRequired()])
  genre = SelectField("Type/Genre", choices=[(gen.id, gen.name) for gen in types])
  song = FileField("Add song", validators=[DataRequired()])
  picture = FileField("Update profile picture", validators=[FileAllowed(["jpg", "png"])])
  submit = SubmitField("Create Single")