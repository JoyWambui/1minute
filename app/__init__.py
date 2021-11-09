from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE

bootsrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
simple = SimpleMDE()

login_manager.session_protection="strong"
login_manager.login_view="authentication.login"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootsrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import authentication as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix="/authentication")
    
    return app