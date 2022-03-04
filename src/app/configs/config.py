import os

HOST = os.getenv('API_BASE_URL', default='0.0.0.0')
PORT = os.getenv('API_PORT', default='80')
DEBUG = bool(os.getenv('API_DEBUG', default='True'))

MONGO_HOST = os.getenv('MONGO_HOST', default='0.0.0.0')
MONGO_PORT = os.getenv('MONGO_PORT', default=27017)
MONGO_DATABASE = os.getenv('MONGO_DATABASE', default='test')
MONGO_USERNAME = os.getenv('MONGO_USERNAME', default=None)
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', default=None)
