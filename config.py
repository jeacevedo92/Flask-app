import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:fl4zk**@localhost:3310/flaskmysql'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
