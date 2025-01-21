import os
from datetime import timedelta
from dotenv import load_dotenv


class Config:

    load_dotenv()

    SECRET_KEY = os.getenv("SECRET_KEY")

    PERMANENT_SESSION_LIFETIME=timedelta(minutes=20)

    SESSION_COOKIE_SECURE = True

    SQLALCHEMY_DATABASE_URI = os.getenv("CONNECTION_STRING")

    RATELIMIT_STORAGE_URI = os.getenv('STORAGE_URI')
    RATELIMIT_STORAGE_OPTIONS = {"socket_connect_timeout": 30}
    RATELIMIT_DEFAULT = "1000 per day"

    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR='/tmp/flask_sessions'

    # app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevents JavaScript access
    SESSION_COOKIE_SAMESITE = 'Lax'  # 'Strict' can block cookies too aggressively