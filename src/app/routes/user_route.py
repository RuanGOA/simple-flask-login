import json

from flask import request, Blueprint
from flask_api import status

from app.controllers import user_controller as controller
from app.utils import response_factory
from app.utils import check_authorization

user = Blueprint('user', __name__)


@user.route('', methods=['POST'])
def create_user():
    try:
        if request.method != 'POST':
            raise Exception()

        return controller.create_user(request)
    except Exception as e:
        return response_factory.make_error(
            http_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='Method not allowed.'
        )


@user.route('/<username>', methods=['GET'])
def search_user(username):
    try:
        if request.method != 'GET':
            raise Exception()

        return controller.search_user(username)
    except Exception as e:
        return response_factory.make_error(
            http_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='Method not allowed.'
        )


@user.route('/login', methods=['POST'])
def login():
    try:
        if request.method != 'POST':
            raise Exception()

        return controller.login(request)
    except Exception as e:
        return response_factory.make_error(
            http_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='Method not allowed.'
        )


@user.route('/test', methods=['GET'])
@check_authorization
def authorized_route():
    try:
        if request.method != 'GET':
            raise Exception()
        
        return controller.authorized_route(request)
    except Exception as e:
        return response_factory.make_error(
            http_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            message='Method not allowed.'
        )
