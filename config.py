class Config:
    """General configuration parent class"""
    pass



class ProdConfig(Config):
    """Production  configuration child class"""

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://bobo:Riptide@localhost/one_minute'


class DevConfig(Config):
    """Development  configuration child class"""
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
}