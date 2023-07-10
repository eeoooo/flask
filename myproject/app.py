from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # app 기본 설정
    app = Flask(__name__)
    app.config.from_object(config)

    # model(ORM)
    db.init_app(app)
    migrate.init_app(db, app)

    # view + controller
    from views import main_views
    app.register_blueprint(main_views.bp)

    return app
