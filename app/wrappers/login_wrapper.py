from functools import wraps
from flask import redirect, session, url_for


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('auth.user_login'))
    return wrap