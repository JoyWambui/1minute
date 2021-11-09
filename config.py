import os
class Config:
    """General configuration parent class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    """Production  configuration child class."""
    pass

class DevConfig(Config):
    """Development  configuration child class."""
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://bobo:Riptide@localhost/one_minute"

    DEBUG = True

class TestConfig(Config):
    """Database test configuration child class."""
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://bobo:Riptide@localhost/one_minute"
    
config_options = {
"development":DevConfig,
"production":ProdConfig,
"test":TestConfig
}