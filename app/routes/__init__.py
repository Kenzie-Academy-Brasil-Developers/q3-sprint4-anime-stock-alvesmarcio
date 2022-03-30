from flask import Flask, Blueprint

from app.routes.anime_routes import bp as anime_bp


bp_v1 = Blueprint("v1", __name__, url_prefix="/v1")

def init_app(app: Flask):
    bp_v1.register_blueprint(anime_bp)
    
    app.register_blueprint(bp_v1)
    