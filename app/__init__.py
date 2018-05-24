from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_simplemde import SimpleMDE
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#configurations
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)
simple = SimpleMDE()
bootstrap = Bootstrap()



# def create_app(config_name):

#     #initializing app
#     app = Flask(__name__)

#     app.config.from_object(config_options[config_name])

#     #initializing flask extensions
#     db.init_app(app)
#     login_manager.init_app(app)
#     simple.init_app(app)
#     bootstrap.init_app(app)

#     #Registering blueprints
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')

#     configure_uploads(app, photos)


#     return app
