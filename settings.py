import os
from datetime import timedelta
from dotenv import load_dotenv


class Config:

    load_dotenv()

    SECRET_KEY=os.getenv('SECRET_KEY')

    PERMANENT_SESSION_LIFETIME=timedelta(minutes=20)

    SESSION_COOKIE_SECURE=True

    SQLALCHEMY_DATABASE_URI=os.getenv('CONNECTION_STRING')

    RATELIMIT_STORAGE_URI = "redis://127.0.0.1:6379"
    RATELIMIT_STORAGE_OPTIONS = {"socket_connect_timeout": 30}
    RATELIMIT_DEFAULT = "100 per day"
