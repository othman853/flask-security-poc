from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required, current_user

import config

application = Flask(__name__)
application.config.from_object(config)

database = SQLAlchemy(application)
from models import User, Role

data_store = SQLAlchemyUserDatastore(database, User, Role)
security = Security(application, data_store)

@application.before_first_request
def create_test_user():

    database.drop_all()
    database.create_all()

    data_store.create_user(email='test@poc.com', password='test')

    database.session.commit()

@application.route('/')
@login_required
def index():

    return render_template('index.j2')
