import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://${{ secrets.USER_DATABASE }}:${{ secrets.PASS_DATABASE }}@${{ secrets.HOST_DATABASE }}:${{ secrets.PORT_DATABASE }}/flaskmysql'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
