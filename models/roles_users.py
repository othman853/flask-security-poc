from initializer import database as db

roles_users = db.Table(

    'roles_users',

    db.Column('user_id', db.Integer(), db.ForeignKey('puser.id')),

    db.Column('role_id', db.Integer(), db.ForeignKey('prole.id'))
)
