from flask import Blueprint, request, jsonify, make_response
from flask_restful import reqparse, Resource, Api
from flask_jwt_extended import (
    create_access_token, unset_jwt_cookies,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies
)

auth_blueprint = Blueprint("auth", __name__)
api = Api(auth_blueprint)


class Login(Resource):

    def post(self):

        """ Login the user """

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        reqdata = parser.parse_args(strict=True)
        
        username = reqdata['username']
        password = reqdata['password']
        
        # Change this to check the user details against a database
        if username != 'test' or password != 'test':
            resp = jsonify({'login': False})
            return make_response(resp, 401)

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        resp = jsonify({'login': True})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return make_response(resp, 200)


class Logout(Resource):

    def post(self):
        
        """ Logout the user """

        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        
        return make_response(resp, 200)


class RefreshToken(Resource):

    @jwt_refresh_token_required
    def post(self):

        """ Refresh the users token (jwt) """
        
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=False)

        resp = jsonify({'refresh': True})
        set_access_cookies(resp, access_token)

        return make_response(resp, 200)
