from flask import render_template, Blueprint, flash, redirect, url_for
from forms import LoginForm, PasswordForm, ProfileForm

bp = Blueprint('user', __name__, template_folder='templates')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "ticket@sample.com" and form.password.data == "user@123":
            flash(f'Welcome to HPI Ticketing System!', 'success')
            return redirect(url_for('user.home'))
        else:
            flash(f'Error login. Please check email and password.', 'danger')

    return render_template('user-login.html', form=form)

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        flash(f'Hi {form.firstname.data}, your information was updated successfully.', 'success')

    return render_template('user-profile.html', form=form)

@bp.route('/change-password', methods=['GET', 'POST'])
def change_pass():
    form = PasswordForm()
    if form.validate_on_submit():
        flash(f'Your password was updated successfully.', 'success')
        return redirect(url_for('user.home'))
    
    return render_template('user-change-pass.html', form=form)

@bp.route('/forgot-password')
def forgot_pass():  
    return render_template('user-forgot-password.html')

@bp.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('user-home.html')