from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims

test_blueprint = Blueprint("test", __name__)
api = Api(test_blueprint)


class Test(Resource):

    @jwt_required
    def get(self):
        ret = {
            'current_identity': get_jwt_identity(),
            'current_roles': get_jwt_claims()['roles']
        }
        return ret, 200
