import os

from flask import Response
from flask_migrate import Migrate

from .database import db
from .model import *
from .routes import *
from .config import Config


app = Flask(__name__)
migrate = Migrate()

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def configure_database(app):
    with app.app_context():
        try:
            engine = db.get_engine()
            if engine.name == 'mysql':
                import pymysql
            db.create_all()
        except Exception as e:
            print(e)
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db-sqlite3')
            db.create_all()


def create_app():
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    
    register_extensions(app)
    configure_database(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(department_bp)

    return app