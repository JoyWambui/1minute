class Config:
    """General configuration parent class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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