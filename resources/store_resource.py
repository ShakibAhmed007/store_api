from flask import Flask,request
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required
from models.store import store

class Store(Resource):
    @jwt_required()
    def get(self):
        return {'All_Stores':store.get_all_store()}

    @jwt_required()
    def post(self):
        data_json = request.get_json(force = True)
        name = data_json['name']
        location = data_json['location']
        store.insert_store_info(name,location)
        return {'Status':'Successful'} , 201

    @jwt_required()
    def put(self):
        data_json = request.get_json(force = True)
        id = data_json['id']
        name = data_json['name']
        location = data_json['location']

        store.update_store_data(int(id),name,location)
        return {'Status':'Successful'} , 201

    @jwt_required()
    def delete(self):
        data_json = request.get_json(force = True)
        id = data_json['id']

        store.delete_store_data(int(id))
        return {'Status':'Successful'} , 201
