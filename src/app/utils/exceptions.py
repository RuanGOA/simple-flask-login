from flask_api import status


class MethodNotAllowedException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_405_METHOD_NOT_ALLOWED

    def __str__(self):
        return 'HTTP method is not allowed.'


class UserNotFoundException(Exception):
    def __init__(self, username):
        self.username = username
        self.status_code = status.HTTP_404_NOT_FOUND

    def __str__(self):
        return f'User {self.username} not found.'


class UserAlreadyExistsException(Exception):
    def __init__(self, username):
        self.username = username
        self.status_code = status.HTTP_409_CONFLICT

    def __str__(self):
        return f'User {self.username} already exists.'


class IncorrectPasswordException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED

    def __str__(self):
        return 'The password is incorrect'


class InvalidTokenException(Exception):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED

    def __str__(self):
        return 'The token is invalid.'


class InvalidAuthorizationHeader(Exception):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED

    def __str__(self):
        return 'Invalid authorization header.'
