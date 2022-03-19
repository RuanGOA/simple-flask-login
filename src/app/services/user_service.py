from app.models import user as user_model
from app.utils import (
    jwt_utils,
    exceptions
)
import bcrypt


def create_user(username, password):
    if user_model.search(username):
        raise exceptions.UserAlreadyExistsException(username)

    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    user = user_model.create(username, hashed_password)

    user.pop('_id', None)
    user.pop('password', None)

    return user


def search_user(username):
    user = user_model.search(username)

    if user:
        user.pop('_id', None)
        user.pop('password', None)
    else:
        raise exceptions.UserNotFoundException(username)

    return user


def login(username, password):
    user = user_model.search(username)

    if user:
        if bcrypt.checkpw(password.encode('utf8'), user.get('password')):
            payload = {
                'username': user.get('username'),
                'password': user.get('password').decode('utf8'),
            }
            return jwt_utils.create_token(payload)
        else:
            raise exceptions.IncorrectPasswordException()
    else:
        raise exceptions.UserNotFoundException(username)


def authorized_route():
    return {
        'data': 'This data is protected with authentication!'
    }
