from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
db.reflect()
ma = Marshmallow(app)

api = Api(app)
api.prefix = '/api'

from routes import *


@app.route('/')
def hello_world():
    return jsonify(api='room apis',
                   version=0.1)


if __name__ == '__main__':
    app.run()
