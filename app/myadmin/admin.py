from flask_admin.contrib.sqla import ModelView
from app import admin, db, user
from app.models import Album, Tracks, Singles, Contact, Type, Team, Newsletter
from flask import url_for, redirect, request, render_template, flash, Blueprint, session, logging
from app.myadmin.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

auth = Blueprint('auth', __name__)

    
@auth.route("/login", methods=["POST", "GET"])
def login():
  if 'user' in session:
    return redirect(url_for("home.homepage"))
  form=LoginForm()
  if form.validate_on_submit():
    pwd = check_password_hash(user["password"], form.password.data)
    print(user["password"])
    if user["username"] == form.username.data and user["password"] == form.password.data:
      session["user"] = form.username.data
      session["admin"] = True
      flash("Login successful", "success")
      return redirect(url_for("admin.index"))
    else:
      flash("Invalid credentials", "danger")
      return redirect(url_for("home.homepage"))
  return render_template("login.html", form=form)
    
    
class TypeModelView(ModelView):
  can_create = True 
  
  def is_accessible(self):
    if 'user' in session:
      return session['admin']
   
  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.login', next=request.endpoint))
    
    
class AdminModelView(ModelView):
  def is_accessible(self):
    if 'user' in session:
      return session['admin']
   
  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.login', next=request.endpoint))
    
    

admin.add_view(AdminModelView(Album, db.session))
admin.add_view(AdminModelView(Tracks, db.session))
admin.add_view(AdminModelView(Singles, db.session))
admin.add_view(AdminModelView(Contact, db.session))
admin.add_view(TypeModelView(Type, db.session))
admin.add_view(AdminModelView(Team, db.session))
admin.add_view(AdminModelView(Newsletter, db.session))
