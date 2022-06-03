from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def page_not_found(error):
    msg = "We’re sorry, the page you have looked for does not exist in our website!. Maybe go to our home page or try to use the navbar?"
    return render_template('error.html', err_msg='page not found', err_code=404, msg=msg), 404


@errors.app_errorhandler(403)
def access_denied(error):
    msg = "We are sorry, you don't have access to this page!. Maybe go to our home page or try to use navbar?"
    return render_template('error.html', err_msg='invalid credentials', err_code=403, msg=msg), 403


@errors.app_errorhandler(500)
def internal_error(error):
    msg = "We are sorry, there is an error with the server side, kindly bear with us for a while!"
    return render_template('error.html', err_msg='internal server error', err_code=500, msg=msg), 500
