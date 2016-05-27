from initializer import database as db
from flask.ext.security import RoleMixin

class Role(db.Model, RoleMixin):

    __tablename__ = 'prole'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
