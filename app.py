from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from auth.api import api as auth_api
from test.api import api as test_api
import config

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

app.config.from_object(config.DevelopmentConfig) 


# Blueprints
app.register_blueprint(
    auth_api.blueprint, url_prefix='/auth')

app.register_blueprint(
    test_api.blueprint, url_prefix=f'{app.config["API_PATH"]}/test')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])