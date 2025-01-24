from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, EmailField
from wtforms.validators import Length, InputRequired, Email, EqualTo, ValidationError
from app.data.repository import check_username_exists, check_email_exists
import re


class RegistrationForm(FlaskForm):

    firstname = StringField('First Name', [InputRequired(), Length(min=1, max=25)])
    lastname = StringField('Last Name', [InputRequired(), Length(min=1, max=25)])
    username = StringField('Username',   [InputRequired(), Length(min=4, max=25)])
    email = EmailField('Email Address', [InputRequired(), Length(min=6, max=35), Email(message=u'Invalid email address')])
    password = PasswordField('Password', [InputRequired(), Length(min=4, max=25)])
    confirm = PasswordField('Repeat Password', [InputRequired(), Length(min=4, max=25), EqualTo('password')])
    accept_tos = BooleanField('I gives GIFeels permission to use my personal data', [InputRequired()])

    def validate_username(form, field):
        if check_username_exists(field.data):
            raise ValidationError('Username already in use')

    def validate_email(form, field):
        if check_email_exists(field.data):
            raise ValidationError('Email already registered')

    def validate_password(form, field):
        if not re.search("(?=.*?[A-Z])", field.data):
            raise ValidationError('Password must have one upper case letter')
        elif not re.search("(?=.*?[0-9])", field.data):
            raise ValidationError('Password must contain one digit')
        elif not re.search("(?=.*?[#?!@$%^&*-])", field.data):
            raise ValidationError('Password must contain one digit')

