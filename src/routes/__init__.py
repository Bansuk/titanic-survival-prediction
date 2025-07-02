"""
Registers the passengers routes with the Flask application.
"""

from flask_smorest import Api
from routes.passenger_routes import passenger_bp


def register_routes(api: Api):
    """
    Registers all application routes.

    Args:
        app (Flask): The Flask application instance.
    """

    api.register_blueprint(passenger_bp)
