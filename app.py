"""Main application module for handling web requests."""

from flask import Flask


def create_app():
    """Create and configure an instance of the Flask application."""
    web_app = Flask(__name__)
    web_app.config.from_mapping(
        SECRET_KEY='',
        DEBUG=False,  # Disable debug mode in production
        SQLALCHEMY_DATABASE_URI='sqlite:///your_database.db',
    )
    return web_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Ensure debug is set to False in production
