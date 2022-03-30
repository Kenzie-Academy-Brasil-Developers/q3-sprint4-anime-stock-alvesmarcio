from app.models import DatabaseConnector
from psycopg2 import sql


class Anime(DatabaseConnector):
    columns = ["id", "anime", "released_date", "seasons"]
    
    def __init__(self, anime, released_date, seasons):
        self.anime = anime
        self.released_date = released_date
        self.seasons = seasons
        
    @classmethod
    def serialize(cls, data: tuple) -> dict:
        """_summary_
            serialize anime data
        Returns:
            _type_: anime object
        """
        return dict(zip(cls.columns, data))
    
    
    def create_anime(self) -> dict:
        """_summary_
            create anime
        Returns:
            _type_: anime object
        """
        (conn, cur) = self.get_conn_cur()
        
        query = """ INSERT INTO animes
                    (anime, released_date, seasons)
                    VALUES
                    (%s, %s, %s)
                    RETURNING *;
                    """
        query_values = (self.anime, self.released_date, self.seasons)
        cur.execute(query, query_values)
        
        conn.commit()
        result = cur.fetchone()
        
        Anime.close_conn_cur()

        return result
    
    
    @classmethod
    def get_animes(cls) -> dict:
        """_summary_
            get all animes
        Returns:
            _type_: anime object
        """
        (conn, cur) = cls.get_conn_cur()
        
        query = """ SELECT * FROM animes; """
        
        cur.execute(query)
        conn.commit()
        result = cur.fetchall()
        
        Anime.close_conn_cur()
        
        return result
    
    @classmethod
    def get_anime(cls, anime_id: int) -> dict:
        """_summary_
            get anime by id
        Returns:
            _type_: anime object
        """
        (conn, cur) = cls.get_conn_cur()
        
        query = """ SELECT * FROM animes WHERE id = %s; """
        query_values = (anime_id,)
        
        cur.execute(query, query_values)
        conn.commit()
        result = cur.fetchone()
        
        Anime.close_conn_cur()
        
        return result
    
    @classmethod
    def update_anime(cls, anime_id: int, payload: dict) -> dict:
        """_summary_
            update anime by id
        Returns:
            _type_: anime object
        """
        
        (conn, cur) = cls.get_conn_cur()
        
        columns = [sql.Identifier(column) for column in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        anime_id = sql.Literal(anime_id)
        
        query = sql.SQL(""" UPDATE animes 
                        SET ({column}) = ROW({value}) 
                        WHERE id = {id}
                        RETURNING *;
                        """).format(id = anime_id,
                                    column = sql.SQL(', ').join(columns), 
                                    value = sql.SQL(', ').join(values))
                        
        cur.execute(query)
        conn.commit()
        result = cur.fetchone()
        
        Anime.close_conn_cur()
        
        return result
    
    @classmethod
    def delete_anime(cls, anime_id: int) -> dict:
        """_summary_
            delete anime by id
        Returns:
            _type_: anime object
        """
        (conn, cur) = cls.get_conn_cur()
        
        query = """ DELETE FROM animes WHERE id = %s RETURNING *; """
        query_values = (anime_id,)
        
        cur.execute(query, query_values)
        conn.commit()
        result = cur.fetchone()
        
        Anime.close_conn_cur()
        
        return result