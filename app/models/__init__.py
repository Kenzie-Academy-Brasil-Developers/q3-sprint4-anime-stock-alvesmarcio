import psycopg2
import os


configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


class DatabaseConnector:
    
    @classmethod
    def get_conn_cur(cls):
        """_summary_

        Returns:
            _type_: Database connection(conn) and cursor(cur)
        """
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()
        return (cls.conn, cls.cur)
    
    
    @classmethod
    def close_conn_cur(cls):
        """_summary_
            close Database connection(conn) and cursor(cur)
        Returns:
            _type_: None
        """
        cls.cur.close()
        cls.conn.close()


def create_table():
      
    (conn, cur) = DatabaseConnector.get_conn_cur()
        
    query = """ CREATE TABLE IF NOT EXISTS animes(
        id BIGSERIAL PRIMARY KEY,
        anime VARCHAR(100) NOT NULL UNIQUE,
        released_date DATE NOT NULL,
        seasons INTEGER NOT NULL
        )
    """
    
    cur.execute(query)
    conn.commit()
    
    cur.close()
    conn.close()
    