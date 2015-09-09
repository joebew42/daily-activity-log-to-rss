from flask import Flask
from rest import settings


class AppBuilder(object):
    def __init__(self):
        self.__app = Flask(__name__)
        self.__app.config.from_object(settings)

    def with_url_rule(self, rule, endpoint, handler, **options):
        self.__app.add_url_rule(rule, endpoint, handler, **options)
        return self

    def build(self):
        return self.__app
