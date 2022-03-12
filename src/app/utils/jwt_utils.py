from app.utils.constants import JWT_EXPIRATION_TIME
from app.configs.config import JWT_SECRET
from datetime import datetime, timedelta, timezone
import jwt


def create_token(payload):
    payload['exp'] = datetime.now(tz=timezone.utc) + timedelta(hours=JWT_EXPIRATION_TIME)
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def is_token_expired(token):
    is_expired = False
    try:
        payload = get_claims(token)
        exp_date = datetime.fromtimestamp(payload.get('exp'))
        is_expired = exp_date < datetime.now()
        return is_expired
    except jwt.exceptions.ExpiredSignatureError as e:
        return is_expired


def validate_token(token, user_data):
    payload = get_claims(token)
    return user_data.get('username') == payload.get('username') and not is_token_expired(token)


def get_claims(token, claims=['exp']):
    try:
        return jwt.decode(token, JWT_SECRET, options={'require': claims}, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError as e:
        pass
