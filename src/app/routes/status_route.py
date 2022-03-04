import json

from flask import Blueprint
from flask_api import status as http_status
from app.utils import response_factory

status = Blueprint('status', __name__)


@status.route('/', methods=['GET'])
def get_status():

    status_body = {
        'status': 'running',
        'service': 'simple-flask-login',
        'version': '1.0.0'
    }

    return response_factory.make_response(
        http_code=http_status.HTTP_200_OK,
        body=status_body
    )
