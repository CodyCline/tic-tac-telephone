'''Settingsuration Settings Based on app phase'''
import os
from configparser import ConfigParser
current_folder = os.path.dirname(os.path.abspath(__file__))
secrets = os.path.join(current_folder, 'keys.cfg')
parser = ConfigParser()
parser.read(secrets)

#Allows only the vuejs frontend to access the server
DEV_ALLOWED_ROUTES = {
    'ORIGINS': [
        parser.get('cors_test', 'test_domain'),
        parser.get('cors_test', 'test_ipaddr'),
    ],
***REMOVED***

PROD_ALLOWED_ROUTES = {
    'ORIGINS': [
        parser.get('cors_prod', 'prod_domain'),
        parser.get('cors_prod', 'prod_ipaddr'),
    ],
***REMOVED***

#Main settings others are used to override
class ServerSettings(object):
    def __init__(self):
        pass
    DEBUG = False
    TESTING = False
    CORS_CONFIG=PROD_ALLOWED_ROUTES
    TWILIO_ACCOUNT_SID = parser.get('twilio', 'account_sid')
    TWILIO_AUTH_TOKEN = parser.get('twilio', 'auth_token')
    TWILIO_SERVER_PHONE = parser.get('twilio', 'server_phone_num')

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