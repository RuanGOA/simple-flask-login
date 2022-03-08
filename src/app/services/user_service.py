from app.models import user as user_model
from app.configs.config import JWT_SECRET
from app.utils import JWT_EXPIRATION_TIME
from datetime import datetime, timedelta
import bcrypt
import jwt


def create_user(username, password):
    if user_model.search(username):
        return None

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

    return user


def login(username, password):
    user = user_model.search(username)
    if user:
        if bcrypt.checkpw(password.encode('utf8'), user.get('password')):
            payload = {
                'username': user.get('username'),
                'password': user.get('password').encode('utf8'),
                'exp': datetime.now() + timedelta(hours=JWT_EXPIRATION_TIME)
            }
            return jwt.encode(payload, JWT_SECRET, algorithm='HS256')
        else:
            raise Exception()
    else:
        raise Exception()
