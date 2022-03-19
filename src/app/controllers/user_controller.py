import json

from flask_api import status

from app.services import user as service
from app.utils import response_factory


def create_user(request):
    username = json.loads(request.get_data()).get('username')
    password = json.loads(request.get_data()).get('password')

    user = service.create_user(username, password)

    return response_factory.make_response(
        http_code=status.HTTP_201_CREATED,
        body=user
    )


def search_user(username):
    user = service.search_user(username)

    return response_factory.make_response(
        http_code=status.HTTP_201_CREATED,
        body=user
    )


def login(request):
    auth_header = request.authorization

    username = auth_header.get('username')
    password = auth_header.get('password')

    token = service.login(username, password)

    return response_factory.make_response(
        http_code=status.HTTP_201_CREATED,
        body={
            'token': token
        }
    )


def authorized_route():
    protected_data = service.authorized_route()

    return response_factory.make_response(
        http_code=status.HTTP_201_CREATED,
        body=protected_data
    )
