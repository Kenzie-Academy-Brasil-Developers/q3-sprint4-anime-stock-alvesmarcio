from flask import Blueprint

from app.controllers import anime_controllers


bp = Blueprint("anime", __name__, url_prefix="/anime")

bp.post("")(anime_controllers.create_anime)
bp.get("")(anime_controllers.get_animes)
bp.get("/<int:anime_id>")(anime_controllers.get_anime)
bp.patch("/<int:anime_id>")(anime_controllers.update_anime)
bp.delete("/<int:anime_id>")(anime_controllers.delete_anime)