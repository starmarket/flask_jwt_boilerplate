class Config(object):
    
    DEBUG = False

    API_VERSION = 1
    API_PATH = f'/api/v{API_VERSION}'
    
    DATABASE = 'path_to_dev_db'

    #JWT
    JWT_TOKEN_LOCATION = ['cookies'] 
    JWT_COOKIE_SECURE = False # Only allow JWT cookies to be sent over https if True.
    JWT_ACCESS_COOKIE_PATH = '/api/' 
    JWT_REFRESH_COOKIE_PATH = '/auth/refresh'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_ACCESS_CSRF_COOKIE_PATH = '/api/'
    JWT_SECRET_KEY = 'super-secret' # Change this


class DevelopmentConfig(Config):

    DEBUG = True
    JWT_COOKIE_CSRF_PROTECT = False


class ProductionConfig(Config):

    DATABASE = 'path_to_prod_db'
