from flask import Flask, jsonify, session
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import sys
from sqlalchemy_utils import database_exists, create_database



app = Flask(__name__)
CORS(app)
app.config.from_object('config')
app.secret_key = 'sessionkey'
db = SQLAlchemy(app)
if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
db.create_all()
db.session.commit()
ma = Marshmallow(app)
migrate = Migrate(app, db)


from models import users
from routes import routes
