import json

from flask_api import status

from app.services import user as service
from app.utils import response_factory


def create_user(request):
    username = json.loads(request.get_data()).get('username')
    password = json.loads(request.get_data()).get('password')

    try:
        user = service.create_user(username, password)

        if not user:
            raise Exception()

        return response_factory.make_response(
            http_code=status.HTTP_201_CREATED,
            body=user
        )

    except Exception:
        return response_factory.make_error(
            http_code=status.HTTP_409_CONFLICT,
            message=f'User {username} already exists.'
        )


def search_user(username):
    try:
        user = service.search_user(username)

        if not user:
            raise Exception()

        return response_factory.make_response(
            http_code=status.HTTP_201_CREATED,
            body=user
        )
    except Exception:
        return response_factory.make_error(
            http_code=status.HTTP_404_NOT_FOUND,
            message=f'Could not find the user {username}.'
        )


def login(request):
    try:
        auth_header = request.authorization
        if not auth_header:
            raise Exception()
        
        username = auth_header.get('username')
        password = auth_header.get('password')

        token = service.login(username, password)

        return response_factory.make_response(
            http_code=status.HTTP_201_CREATED,
            body={
                'token': token
            }
        )

    except Exception as e:
        return response_factory.make_error(
            http_code=status.HTTP_404_NOT_FOUND,
            message=f''
        )
