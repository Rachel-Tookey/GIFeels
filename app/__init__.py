from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
oauth = OAuth()
bcrypt = Bcrypt()


def create_app(config_class=None, test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    if test_config:
        app.config.update(test_config)

    app.jinja_env.lstrip_blocks = True

    app.jinja_env.trim_blocks = True

    db.init_app(app)
    oauth.init_app(app)
    bcrypt.init_app(app)

    Migrate(app, db)

    from app.routes import main

    app.register_blueprint(main)

    return app