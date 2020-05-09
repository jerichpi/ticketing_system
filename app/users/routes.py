from flask import render_template, Blueprint

bp = Blueprint('user', __name__, template_folder='templates')

@bp.route('/login')
def login():
    return render_template('user-login.html')

@bp.route('/forgot-password')
def forgot_pass():
    return render_template('user-forgot-password.html')

@bp.route('/home')
def home():
    return render_template('user-home.html')