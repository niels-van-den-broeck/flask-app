from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

article_session = db.Table('article_id', db.Column('article_id', db.Integer, db.ForeignKey('article.id')),db.Column('session_id', db.Integer, db.ForeignKey('session.id')))


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
