import json

from flask import request, Blueprint
from flask_api import status as http_status
from app.utils import exceptions
from app.utils import response_factory
from app.utils.decorators import exception_handler

status = Blueprint('status', __name__)


@status.route('/', methods=['GET'])
@exception_handler
def get_status():
    if request.method != 'GET':
        raise exceptions.MethodNotAllowedException()

    status_body = {
        'status': 'running',
        'service': 'simple-flask-login',
        'version': '1.0.0'
    }

    return response_factory.make_response(
        http_code=http_status.HTTP_200_OK,
        body=status_body
    )
