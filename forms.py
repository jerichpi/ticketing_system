from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class ProfileForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    middle_initial = StringField("Middle Initial", validators=[Length(min=1, max=4)])
    submit = SubmitField("Save Changes")

class PasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Change password")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email("This field requires Email Address")])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")