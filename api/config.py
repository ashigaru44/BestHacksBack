import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KEY = "\xaf\x07q\xd6o\x1e/jph\xa6\xdb\xaa}\xb9\xeay\xd5\xc8\x05\xdf\xaa#\x82"
class BaseConf(object):
    ORIGINS = ["*"]
    SECRET_KEY = KEY
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")

class DevelopmentConf(BaseConf):

    DEBUG = True
    TESTING = False
    ENV = "development"
    APPNAME = "quizDev"

class ProductionConf(BaseConf):

    SERVER_NAME = 'localhost:8080'
    DEBUG = False
    TESTING = False
    ENV = "production"
    APPNAME = "quizProd"

class TestConf(BaseConf):

    SERVER_NAME = 'localhost.localdomain:6000'
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(BASE_DIR, "test_app.db")
    DEBUG = True
    TESTING = True
    ENV = "testing"
    APPNAME = "quizTest"

    