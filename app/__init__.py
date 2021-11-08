from flask import Flask, app
from config import DevConfig, config_options

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    return app