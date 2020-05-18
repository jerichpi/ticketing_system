from flask import render_template, Blueprint, flash, redirect, url_for
from forms import LoginForm, PasswordForm, ProfileForm

bp = Blueprint('user', __name__, template_folder='templates')

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('user-login.html', form=form)

@bp.route('/forgot-password')
def forgot_pass():
    return render_template('user-forgot-password.html')

@bp.route('/home', methods=['GET', 'POST'])
def home():
    passform = PasswordForm()
    proform = ProfileForm()
    if proform.validate_on_submit():
        flash(f'Hi {proform.firstname.data}, your info was successfully updated.', 'success')
        return redirect(url_for('user.home'))
        
    return render_template('user-home.html', passform=passform, proform=proform)