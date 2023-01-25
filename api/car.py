from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.cars import Cars

car_api = Blueprint('car_api', __name__,
                   url_prefix='/api/cars')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(car_api)

class CarsAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            id = body.get('id')
            if id is None :
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Cars(name=name, 
                      car=car, id=id,)
            
            ''' Additional garbage error checking '''
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            car = uo.create()
            # success returns json of user
            if car:
                return jsonify(car.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            cars = Cars.query.all()    # read/extract all users from database
            json_ready = [car.read() for car in cars]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')