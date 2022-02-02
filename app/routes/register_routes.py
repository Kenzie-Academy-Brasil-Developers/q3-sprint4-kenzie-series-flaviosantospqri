from flask import Blueprint, request, jsonify
from http import HTTPStatus
import psycopg2

bp = Blueprint('series', __name__, url_prefix='/api')

@bp.post('/series')
def create():
   data = request.get_json()
   
   conn = psycopg2.connect(host='localhost', database='ka_series_db', user='flavio', password='1234')
   
   
   cur = conn.cursor()

   cur.execute(
    """
    CREATE TABLE IF NOT EXISTS ka_series(
        id BIGSERIAL PRIMARY KEY,
        serie VARCHAR(100),
        seasons INTEGER NOT NULL,
        released_date DATE NOT NULL,
        genre VARCHAR(50) NOT NULL,
        imdb_rating FLOAT NOT NULL
    );
    """
   )
   serie = (data["serie"].title(),data["seasons"],data["released_date"],data["genre"],data["imdb_rating"])
   query = ('INSERT INTO ka_series (serie, seasons, released_date, genre, imdb_rating) VALUES (%s, %s, %s, %s, %s)')
   cur.execute(query, serie)

   conn.commit()
   cur.close()
   conn.close()

   return {'Data': data}, HTTPStatus.CREATED