from flask import Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required

test_blueprint = Blueprint("test", __name__)
api = Api(test_blueprint)

class Test(Resource):

    @jwt_required
    def get(self):
        return "Yihaaaw!"
