import json

from flask import request, Blueprint
from flask_api import status

from app.controllers import user_controller as controller
from app.utils import response_factory
from app.utils import exceptions
from app.utils.decorators import (
    check_authorization,
    exception_handler
)

user = Blueprint('user', __name__)


@user.route('', methods=['POST'])
@exception_handler
def create_user():
    if request.method != 'POST':
        raise exceptions.MethodNotAllowedException()

    return controller.create_user(request)


@user.route('/<username>', methods=['GET'])
@exception_handler
def search_user(username):
    if request.method != 'GET':
        raise exceptions.MethodNotAllowedException()

    return controller.search_user(username)


@user.route('/login', methods=['POST'])
@exception_handler
def login():
    if request.method != 'POST':
        raise exceptions.MethodNotAllowedException()

    return controller.login(request)


@user.route('/test', methods=['GET'])
@exception_handler
@check_authorization
def authorized_route():
    if request.method != 'GET':
        raise exceptions.MethodNotAllowedException()

    return controller.authorized_route()
