from os import getenv
from flask import Flask
from flask_bootstrap import Bootstrap4
from container import Container
from core.constants.app_metadata import APP_NAME


class StartUp(object):

    @staticmethod
    def build() -> Flask:
        app = Flask(APP_NAME)
        app.env = getenv('ENVIRONMENT', 'development')
        app.container = Container()
        bootstrap = Bootstrap4()
        bootstrap.init_app(app)

        return app
