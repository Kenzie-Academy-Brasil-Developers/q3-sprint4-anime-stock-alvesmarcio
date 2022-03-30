from flask import Flask
from app import routes
from app.models import create_table


create_table()

def create_app():
    app = Flask(__name__)
    
    """_summary_

    Args:
        no args

    Returns:
        _type_: flask app
    """
    routes.init_app(app)
    return app