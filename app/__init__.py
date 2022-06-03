from flask import Flask, redirect, url_for, request, session
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

user = {
  "username": "admin", 
  #"password": generate_password_hash("goodluck")
  "password": "goodluck",
  "name": "Kiss Daniel"
  }

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


class MyAdminIndexView(AdminIndexView):
  def is_accessible(self):
    if 'user' in session:
      return session['admin']
    
  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.login', next=request.endpoint))

admin = Admin(template_mode='bootstrap4', index_view=MyAdminIndexView())


def create_app():
    app = Flask(__name__)
    # app.config.from_object(DevelopmentConfig if os.environ.get(
    #     "PRODUCTION").lower() == 'true' else DevelopmentConfig)
    app.config.from_object(DevelopmentConfig)
        
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True 
    
    db.init_app(app)
    admin.init_app(app)

    from app.errors.handlers import errors
    from app.home.routes import home
    from app.myadmin.admin import auth

    app.register_blueprint(errors)
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app


# After 'Create app'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'officialcontact788@gmail.com'
app.config['MAIL_PASSWORD'] = 'ysnxhvlbzjpdynve'

mail = Mail(app)

app.config['MAIL_SUBJECT_PREFIX'] = '[MUSIC]'
app.config['MAIL_SENDER'] = 'MUSIC - <officialcontact788@gmail.com>'