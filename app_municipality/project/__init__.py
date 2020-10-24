import os
import marshmallow
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def register_blueprints(app):
    from project.municipalities.endpoints.municipalities import municipality_blueprint

    app.register_blueprint(municipality_blueprint)


def register_error_handlers(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(ex):
        return ex.messages, 400


def create_app():
    app = Flask(__name__)

    app_config = os.getenv('APP_CONFIG')
    app.config.from_object(app_config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)
    register_error_handlers(app)

    return app
