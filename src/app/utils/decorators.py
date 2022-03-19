from app.models import user as user_model
from app.utils import jwt_utils
from app.utils import response_factory
from functools import wraps
from app.utils import exceptions
from flask import request


def check_authorization(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]
            payload = jwt_utils.get_claims(token)

            user = user_model.search(payload.get('username'))
            if not (user and jwt_utils.validate_token(token, user)):
                raise exceptions.InvalidTokenException()
        else:
            raise exceptions.InvalidAuthorizationHeader()

        return func(*args, **kwargs)

    return wrap


def exception_handler(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            return response_factory.make_error(
                http_code=exception.status_code,
                message=str(exception)
            )

    return wrap
