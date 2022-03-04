from app.routes.status_route import status
from app.routes.user_route import user

def create_routes(app):
    app.register_blueprint(status, url_prefix='/status')
    app.register_blueprint(user, url_prefix='/user')
