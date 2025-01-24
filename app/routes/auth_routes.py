from app.data.repository import *
from app.forms.registration_form import RegistrationForm
from flask import render_template, request, redirect, session, url_for, Blueprint
from app.utils.date_utils import get_utc_date
from app.settings.oauth_providers import googleOauth
from app import bcrypt
from app.utils.flask_helpers import flash_error, flash_notification
from app.wrappers.login_wrapper import login_required

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user_form = {}
        for item in ["firstname", "lastname", "uname", "email", "password", "confirm", "accept_tos"]:
            user_form[item] = request.form.get(item)
        user_form['password'] = bcrypt.generate_password_hash(user_form['password']).decode('utf-8')
        add_new_global_user(user_form['email'], user_form['uname'])
        user_id = get_user_id_by_email(user_form["email"])
        add_new_local_user(user_id, user_form)
        flash_notification("Your account has been created. Please login.")
        return redirect('/login')
    return render_template("register.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        session.clear()
        username = request.form.get('uname')
        password = request.form.get('password')
        if not check_username_exists(username):
            flash_error("This username does not exist")
        else:
            user_id = get_user_id_by_username(username)
            stored_password = get_password(user_id)
            if not bcrypt.check_password_hash(stored_password, password):
                flash_error("Username and Password do not match")
            else:
                session['user'] = username
                session['user_id'] = get_user_id_by_username(username)
                session['date'] = get_utc_date()
                return redirect('/')
    return render_template("login.html")


@auth.route('/login/google')
def login_google():
    return googleOauth.authorize_redirect(redirect_uri=url_for("auth.authorize_google", _external=True))


@auth.route('/authorize/google')
def authorize_google():
    token = googleOauth.authorize_access_token()
    userinfo_endpoint = googleOauth.server_metadata['userinfo_endpoint']
    user_info = googleOauth.get(userinfo_endpoint).json()

    if not check_email_exists(user_info['email']):
        add_new_global_user(email=user_info['email'])
        user_id = get_user_id_by_email(user_info['email'])
        add_new_auth_user(user_id, user_info)
    else:
        user_id = get_user_id_by_email(user_info['email'])

    session['oauth_token'] = token
    session['user_id'] = user_id
    session['date'] = get_utc_date()
    session['user'] = user_info['email']
    return redirect("/")


@auth.route('/logout')
@login_required
def user_logout():
    session.clear()
    flash_notification("You have been logged out. See you soon!")
    return redirect('/')
