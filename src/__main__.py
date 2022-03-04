import app
from app.configs import config


def main():
    api = app.start_app()
    api.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == '__main__':
    main()
