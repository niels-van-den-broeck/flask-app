from flask import Flask
from core.routes import routes
from core.models import db

def create_app():
    app = Flask(__name__)
    app.config.update(
        # SECRET_KEY='very-secret-key',  # secret key used to sign the session cookie
        # SESSION_COOKIE_NAME='test-session',  # sets cookie name
        # PERMANENT_SESSION_LIFETIME=timedelta(days=31), # sets cookie expiry
        # please get this from os environment...
        SESSION_PERMANENT=False,
        SESSION_TYPE='sqlalchemy',
        SESSION_SQLALCHEMY_TABLE='sessions',
        SQLALCHEMY_DATABASE_URI='mysql://root@localhost:3306/news_app',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    app.register_blueprint(routes)

    return app

app = create_app()

with app.app_context():
    db.init_app(app)
    db.create_all()


# @app.before_request
# def before_request():
#     # Check if session is initialized, if not initialize it
#     session['id'] = uuid.uuid4()

# @app.route('/login', methods=['POST'])
# def loginHandler():
#     username = request.json.username
#     password = request.json.password

#     user = query('SELECT * FROM users WHERE username = ? ', username)

#     if user is None:
#         return 'User not found', 400

#     if hash_matches(password, user.password_hash):
#         session['user_id'] = user.id # save user id in session so we know who is logged in

#         return 'Logged in', 200

# @app.route('/articles')
# def articlesHandler():
#     nonVisitedArticles = query('SELECT * FROM articles WHERE id NOT IN (SELECT article_id FROM visits WHERE session_id = ?)')

#     return 'Articles'
