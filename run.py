import os
from flask import Flask
from flask_minify import Minify
from dotenv import load_dotenv

from app import create_app
from app.config import *

load_dotenv()

app = create_app()
Minify(app=app, html=True, js=False, cssless=True)
if __name__ == "__main__":
    app.run(host=Config.FLASK_RUN_HOST, port=Config.FLASK_RUN_PORT)