from datetime import datetime
from app import db
from flask import current_app as app

  
class Album(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
  date_created = db.Column(db.DateTime(120), nullable=False, default= datetime.utcnow)
  tracks = db.relationship("Tracks", backref="album", lazy=True, cascade="all, delete")
  
  def __repr__(self):
    return f"ALBUM: {self.title}"


class Tracks(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  date_created = db.Column(db.DateTime(120), nullable=False, default= datetime.utcnow)
  song_path = db.Column(db.String(255), nullable=False)
  typ = db.Column(db.Integer, db.ForeignKey("type.id"), nullable=False)
  album_id = db.Column(db.Integer, db.ForeignKey("album.id"), nullable=False)
  
  def __repr__(self):
    return f"TRACK: {self.title}, Album:- {self.album.title}"
  
class Singles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
  song_path = db.Column(db.String(255), nullable=False)
  typ = db.Column(db.Integer, db.ForeignKey("type.id"), nullable=False)
  date_created = db.Column(db.DateTime(120), nullable=False, default= datetime.utcnow)
  
  def __repr__(self):
    return f"SINGLE: {self.title}"
  
  
class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True) 
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.Integer, nullable=True)
  message = db.Column(db.String(250), nullable=False)
  date = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
  read = db.Column(db.Boolean(), default=False)
  
  def is_read(self):
    return self.read
  
  def is_not_read(self):
    return not self.read
  
  
class Newsletter(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), nullable=False)
    
    
class Type(db.Model):
  id = db.Column(db.Integer, primary_key=True) 
  name = db.Column(db.String(25), nullable=False)
  tracks = db.relationship("Tracks", backref="type", lazy=True) 
  singles = db.relationship("Singles", backref="type", lazy=True) 
  
  def __repr__(self):
    return self.name
  
  
class Team(db.Model):
  id = db.Column(db.Integer, primary_key=True) 
  name = db.Column(db.String(50), nullable=False)
  specialty = db.Column(db.String(25), nullable=False)
  image_file = db.Column(db.String(50), nullable=False, default="default.jpg")