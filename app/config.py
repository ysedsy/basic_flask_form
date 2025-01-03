from dotenv import load_dotenv
import os
import urllib

load_dotenv()

class Config:
    FLASK_APP = "app.py"
    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = True

    DB_ENGINE = os.environ.get("DB_ENGINE")
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")

    if not DB_ENGINE:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///".format(
            os.path.join(os.path.dirname(__file__), f"{DB_NAME}.db")
        )
    else:
        SQLALCHEMY_DATABASE_URI = f"{DB_ENGINE}+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"