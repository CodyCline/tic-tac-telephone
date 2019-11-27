'''Settingsuration Settings Based on app phase'''
import os
from configparser import ConfigParser
current_folder = os.path.dirname(os.path.abspath(__file__))
secrets = os.path.join(current_folder, 'keys.cfg')
parser = ConfigParser()
parser.read(secrets)

DEV_ALLOWED_ROUTES = {
    'ORIGINS': [
        'http://localhost:8080',  # Vue Frontend
        'http://127.0.0.1:8080',  # Vue Frontend
    ],
***REMOVED***

PROD_ALLOWED_ROUTES = {
    'ORIGINS': [
        str(parser.get('file', 'front_end_domain')),  # Vue Frontend App
    ],
***REMOVED***

#Main settings others are used to override
class ServerSettings(object):
    def __init__(self):
        pass
    DEBUG = False
    TESTING = False
    CORS_CONFIG=DEV_ALLOWED_ROUTES
    TWILIO_ACCOUNT_SID = parser.get('file', 'account_sid')
    TWILIO_AUTH_TOKEN = parser.get('file', 'auth_token')
    TWILIO_SERVER_PHONE = parser.get('file', 'server_phone_num')

class DevelopmentSettings(ServerSettings):
    DEBUG = True
    TESTING = True
    CORS_CONFIG = DEV_ALLOWED_ROUTES
    

class TestingSettings(ServerSettings):
    DEBUG = False
    TESTING = True
    CORS_CONFIG = DEV_ALLOWED_ROUTES

class ProductionSettings(ServerSettings):
    DEBUG = False
    TESTING = False
    CORS_CONFIG = PROD_ALLOWED_ROUTES