from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.facts import Facts

fact_api = Blueprint('fact_api', __name__,
                   url_prefix='/api/facts')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(fact_api)

class FactsAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate car
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'car is missing, or is less than 2 characters'}, 210
            # validate uid
            industry = body.get('industry')
            if industry is None or len(industry) < 2:
                return {'message': f'car is missing, or is less than 2 characters'}, 210
            # look for industry and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Facts(car=car, industry=industry)
            
            ''' Additional garbage error checking '''
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            Fact = uo.create()
            # success returns json of user
            if Fact:
                return jsonify(Fact.read())
            # failure returns error
            return {'message': f'Processed {car}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            facts = Facts.query.all()    # read/extract all users from database
            json_ready = [Fact.read() for Fact in facts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        
    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            id = body.get('id')
            uo = Facts(id=id)
            Fact = uo.delete()
            if Fact:
                return jsonify(Fact)
            # failure returns error
            return {'message': f'Processed {id}, either a format error or User ID is duplicate'}, 210

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')