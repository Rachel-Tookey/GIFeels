from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, EmailField, validators
from wtforms.validators import Length, InputRequired, Email, EqualTo, ValidationError, Regexp
import email_validator


class RegistrationForm(FlaskForm):

    FirstName = StringField('First Name', [InputRequired(), Length(min=1, max=25), Regexp(regex='(?=.*?[A-Z])', message='Password must contain one special character')])
    LastName = StringField('Last Name', [InputRequired(), Length(min=1, max=25)])
    Username = StringField('Username',   [InputRequired(), Length(min=4, max=25)])
    email = EmailField('Email Address', [InputRequired(), Length(min=6, max=35), Email(message=u'Invalid email address')])
    password = PasswordField('Password', [InputRequired(), Length(min=4, max=25), Regexp(regex='(?=.*?[A-Z])', message='Password must contain one special character')])
    confirm = PasswordField('Repeat Password', [InputRequired(), Length(min=4, max=25), EqualTo('password')])
    accept_tos = BooleanField('I gives GIFeels permission to use my personal data', [InputRequired()])


