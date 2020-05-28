from flask import render_template, Blueprint, flash, redirect, url_for
from forms import LoginForm

bp = Blueprint('admin', __name__, template_folder='templates')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin@123':
            flash(f'Welcome to HPI Ticketing System.', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash(f'Login error. Please check email and password.', 'danger')

    return render_template("login.html", form=form)

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