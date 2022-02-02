from flask import Flask, Blueprint
from app import routes

def create_app():
    app = Flask(__name__)
    routes.init_app(app)
    return app


