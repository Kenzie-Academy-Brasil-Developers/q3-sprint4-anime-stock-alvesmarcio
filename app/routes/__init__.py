from flask import Flask, Blueprint

from app.routes.anime_routes import bp as anime_bp


bp_home = Blueprint("home", __name__, url_prefix="")

def init_app(app: Flask):
    bp_home.register_blueprint(anime_bp)
    
    app.register_blueprint(bp_home)
    