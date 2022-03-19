from flask import Flask
from flask_cors import CORS

from app.routes import create_routes


def start_app():
    app = Flask(__name__)

    create_routes(app)

    return app
