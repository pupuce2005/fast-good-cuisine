from flask import Flask
from app.config import Config
from app.database import db
from app.routes import main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()

    return app