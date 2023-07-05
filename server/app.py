from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db

from flask_restful import Api, Resource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False # configures JSON responses to print on indented lines

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Create your classes here
