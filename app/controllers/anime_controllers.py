from flask import request, jsonify
from http import HTTPStatus
from app.models.anime_models import Anime
from psycopg2.errors import UniqueViolation


def create_anime() -> dict:
    """_summary_
        create anime
    Returns:
        _type_: anime object
    """
    try:
        anime = request.get_json()["anime"]
        released_date = request.get_json()["released_date"]
        seasons = request.get_json()["seasons"]

        new_anime = Anime(anime.title(), released_date, seasons)
        
        result = new_anime.create_anime()
        
        return jsonify(Anime.serialize(result)), HTTPStatus.CREATED
    
    except UniqueViolation:
        return {"error": "Anime already exists"}, HTTPStatus.CONFLICT
        
    except:
        available_keys = ["anime", "released_date", "seasons"]
        wrong_keys_sended = [key for key in request.json.keys() if key not in available_keys]
        
        return jsonify({"available_keys": available_keys, "wrong_keys_sended": wrong_keys_sended}), HTTPStatus.UNPROCESSABLE_ENTITY
    
    
def get_animes() -> dict:
    """_summary_
        get all animes
    Returns:
        _type_: anime object
    """
    animes = Anime.get_animes()
    result = [Anime.serialize(anime) for anime in animes]
    
    return jsonify({"data": result}), HTTPStatus.OK
    
    
def get_anime(anime_id: int) -> dict:
    """_summary_
        get anime
    Returns:
        _type_: anime object
    """
    try:
        animes = Anime.get_anime(anime_id)
        result = Anime.serialize(animes)
        
        return jsonify({"data": [result]}), HTTPStatus.OK
    except:
        
        return jsonify({"message": "Anime not found"}), HTTPStatus.NOT_FOUND
    
    
def update_anime(anime_id: int) -> dict:
    """_summary_
        update anime
    Returns:
        _type_: anime object
    """
    try:
        payload = request.get_json()
        update_anime = Anime.update_anime(anime_id, payload)
        
        if not update_anime:
            return jsonify({"error": "Anime not found"}), HTTPStatus.NOT_FOUND
        
        result = Anime.serialize(update_anime)
        
        return jsonify(result), HTTPStatus.OK
    except:
        available_keys = ["anime", "released_date", "seasons"]
        wrong_keys_sended = [key for key in request.json.keys() if key not in available_keys]
    
        return jsonify({"available_keys": available_keys, "wrong_keys_sended": wrong_keys_sended}), HTTPStatus.UNPROCESSABLE_ENTITY


def delete_anime(anime_id: int) -> dict:
    """_summary_
        delete anime
    Returns:
        _type_: anime object
    """
    anime = Anime.delete_anime(anime_id)
    
    if not anime:
        return jsonify({"error": "Anime not found"}), HTTPStatus.NOT_FOUND
    
    return "", HTTPStatus.NO_CONTENT