from flask import Blueprint, render_template, request, flash, current_app, redirect, url_for
from app import db, create_app, app, user
from app.models import Newsletter, Contact, Singles, Tracks, Album
from random import randint
from werkzeug.utils import secure_filename
import os

home = Blueprint('home', __name__)

from app.home.forms import AlbumForm, TrackForm, SinglesForm

@home.route('/home')
@home.route('/', methods=['GET', 'POST'])
def homepage():
  # NEWSLETTER 
  if request.method == "POST":
    email = request["news_email"]
    news = Newsletter(email = email)
    db.session.add(news)
    db.session.commit()
    flash("Subscribe successful", "success")
  if request.method == "POST":
    name = request["name"]
    email = request["email"]
    phone = request["phone"]
    message = request["message"]
    cont = Contact(name = name, email=email, phone=phone, message = message)
    db.session.add(cont)
    db.session.commit()
    flash("Message sent successfully", "success")
  albums = Album.query.order_by(Album.id.desc()).all()
  singles = Singles.query.order_by(Singles.id.desc()).limit(5)
    
  return render_template('home.html', title='Home', albums = albums, name=user["name"], singles=singles)


@home.route('/singles')
def singles():
  singles = Singles.query.order_by(Singles.id.desc()).limit(5)
  return render_template('singles.html', title='Singles', name=user["name"], singles=singles)


@home.route('/albums')
def albums():
  albums = Album.query.order_by(Album.id.desc()).all()
  return render_template('albums.html', title='Albums', albums=albums, name=user["name"])

@home.route("/create-album", methods=["POST", "GET"])
def create_album():
  form=AlbumForm()
  picture=None
  if form.validate_on_submit():
    if form.picture.data:
      pic = form.picture.data
      picture=secure_filename(str(pic))
      pic.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/img/album", picture))
      album = Album(
        title=form.title.data,
        image_file=picture
        )
      db.session.add(album)
      db.session.commit()
    else:
      album = Album(
        title=form.title.data
        )
      db.session.add(album)
      db.session.commit()
    flash("Album created successfully", "success")
    return redirect(url_for("home.add_track", album_id = album.id))
  return render_template("admin/new_album.html", form=form)
  
  
@home.route("/track/<int:album_id>/new", methods=["GET", "POST"])
def add_track(album_id):
  form=TrackForm()
  album = Album.query.get_or_404(album_id)
  if form.validate_on_submit():
    song = form.song.data
    filename = secure_filename(str(song))
    song.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/audio", filename))
    track = Tracks(
      title = form.title.data,
      song_path = filename,
      typ = form.genre.data,
      album_id = album.id)
    db.session.add(track)
    db.session.commit()
    flash("Track created successfully", "success")
  return render_template("admin/new.html", form=form, title="Add Track", legend="Add Track")
  
  
@home.route("/single/new", methods=["GET", "POST"])
def add_single():
  form=SinglesForm()
  if form.validate_on_submit():
    song = form.song.data
    filename = secure_filename(str(song))
    song.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/audio", filename))
    if form.picture.data:
      picture=form.picture.data
      file = secure_filename(str(picture))
      picture.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/img/singles", file))
      single = Singles(
        title = form.title.data,
        image_file=file,
        typ = form.genre.data,
        song_path = filename)
      db.session.add(single)
      db.session.commit()
    else:
      single = Singles(
        title = form.title.data,
        typ = form.genre.data,
        song_path = filename)
      db.session.add(single)
      db.session.commit()
      
    flash("Single created successfully", "success")
    return redirect(url_for("home.homepage"))
  return render_template("admin/new.html", form=form, title="New Single", legend="Add Track")