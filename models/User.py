from flask.ext.security import UserMixin
from initializer import database as db
from models import roles_users

class User(db.Model, UserMixin):

    __tablename__ = 'puser'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship(
        'Role',
        secondary='roles_users',
        backref = db.backref('users', lazy='dynamic')
    )
