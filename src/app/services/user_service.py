from app.models import user as user_model
from app.configs.config import JWT_SECRET
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
            user.pop('_id', None)
            user['password'] = user.get('password').decode('utf8')
            return jwt.encode(user, JWT_SECRET, algorithm='HS256')
        else:
            raise Exception()
    else:
        raise Exception()
