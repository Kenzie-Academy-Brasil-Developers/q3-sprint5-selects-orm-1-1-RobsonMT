from flask import Blueprint, Flask

from .grupos_route import bp as bp_grupos

api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    api.register_blueprint(bp_grupos)

    app.register_blueprint(api)
