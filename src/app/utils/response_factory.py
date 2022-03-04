import json

from flask import Response
from flask_api import status


def make_response(http_code, body=None):
    return Response(
        json.dumps(body, ensure_ascii=False).encode('utf8'),
        status=http_code,
        mimetype='application/json'
    )


def make_error(http_code, message='Something went wrong'):
    return Response(
        json.dumps({'error': message}, ensure_ascii=False).encode('utf8'),
        status=http_code,
        mimetype='application/json'
    )
