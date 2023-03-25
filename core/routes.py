from flask import Blueprint, jsonify
from core.models import Articles

routes = Blueprint( 'routes', __name__)

@routes.route('/')
def home():
    return 'Home'

@routes.route('/articles')
def articles():
    articles = Articles.query.all()

    return jsonify([article.serialize for article in articles])
