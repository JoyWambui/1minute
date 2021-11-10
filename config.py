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
    SQLALCHEMY_DATABASE_URI = "postgres://rnddqlqvyzcjva:be4d83b2e0fcf55df74b5bc9e5108ca187f98623d9e1c358caeef7f9a11a8129@ec2-3-227-149-67.compute-1.amazonaws.com:5432/d777gb4fitnjb0"
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
class TestConfig(Config):
    """Database test configuration child class."""
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://bobo:Riptide@localhost/one_minute_test"

class DevConfig(Config):
    """Development  configuration child class."""
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://bobo:Riptide@localhost/one_minute"

    DEBUG = True
    
config_options = {
"development":DevConfig,
"production":ProdConfig,
"test":TestConfig
}