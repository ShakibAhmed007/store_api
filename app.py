from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import verify,identity
from resources.store_resource import Store


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/store'
app.config['SECRET_KEY'] = 'super_secret'
api = Api(app)

jwt = JWT(app,verify,identity)
api.add_resource(Store , '/store')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug = True)
