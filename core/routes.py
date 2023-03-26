from flask import Blueprint, jsonify, session
from core.models import Articles
from sqlalchemy import select

routes = Blueprint( 'routes', __name__)

@routes.route('/')
def home():
    return 'Home'

@routes.route('/articles')
def articles():
    articles = select(Articles).all()
    session.test = True

    return jsonify([article.serialize for article in articles])

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