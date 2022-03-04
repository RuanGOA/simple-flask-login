from app.models import user as user_model


def create_user(username, password):
    if user_model.search(username):
        return None

    user = user_model.create(username, password)

    return user


def search_user(username):
    user = user_model.search(username)

    return user
