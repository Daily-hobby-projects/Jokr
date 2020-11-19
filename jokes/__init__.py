from flask import Flask
from .config import DevConfig
from .utils.database import db
from .models.jokes import Joke
from .pages.routes import app_bp
from .api.routes import api_bp


def create_app():
    app=Flask(__name__,static_folder='./pages/static')

    app.config.from_object(DevConfig)

    app.register_blueprint(app_bp,url_prefix='/')

    app.register_blueprint(api_bp,url_prefix='/api')

    db.init_app(app)

    with app.app_context():
        @app.shell_context_processor
        def make_shell_context():
            return {
                'app':app,
                'db':db,
                'Joke':Joke
            }

    return app