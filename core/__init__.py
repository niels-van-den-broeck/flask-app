from flask import Flask, session
from flask_session import Session
from core.routes import routes
from core.models import db
from datetime import timedelta
from uuid import uuid4

def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY='very-secret-key',  # secret key used to sign the session cookie
        SESSION_COOKIE_NAME='test-session',  # sets cookie name
        PERMANENT_SESSION_LIFETIME=timedelta(days=31),  # sets cookie expiry
        SESSION_TYPE='sqlalchemy',
        SESSION_SQLALCHEMY=db,
        # please get this from os environment...
        SQLALCHEMY_DATABASE_URI='mysql://root@localhost:3306/news_app',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    app.register_blueprint(routes)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        Session(app)

    return app

app = create_app()


@app.before_request
def before_request():
    # Check if session is initialized, if not initialize it
    if session.get('user') is None:
        session['user'] = uuid4()
