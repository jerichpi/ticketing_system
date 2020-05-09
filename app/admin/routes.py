from flask import render_template, Blueprint

bp = Blueprint('admin', __name__, template_folder='templates')

@bp.route('/login')
def login():
    return render_template("login.html")

@bp.route('/dashboard')
def dashboard():
    active = 1
    return render_template("dashboard.html", dashactive=active)

@bp.route('/forgot-password')
def forgotpw():
    return render_template("forgot-password.html")

@bp.route('/change-password')
def changepw():
    return render_template("recover-password.html")

@bp.route('/ticket')
def ticket():
    active = 1
    return render_template("ticket.html", active=active)

@bp.route('/user')
def user():
    active = 1
    return render_template("user.html", useractive=active)