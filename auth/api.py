from .handlers import api, Login, Logout, RefreshToken

api.add_resource(Login, '/')
api.add_resource(Logout, '/logout')
api.add_resource(RefreshToken, '/refresh')
