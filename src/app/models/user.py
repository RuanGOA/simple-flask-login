from app.configs import db_connection


def search(username):
    query = {'username': username}
    user = db_connection.user.find_one(query)

    return user


def create(username, password):
    user = {'username': username, 'password': password}
    db_connection.user.insert_one(user)

    return user


def update():
    pass


def delete():
    pass
