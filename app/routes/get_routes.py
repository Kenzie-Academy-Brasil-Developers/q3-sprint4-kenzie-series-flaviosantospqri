from flask import Blueprint, request, jsonify
from http import HTTPStatus
import psycopg2

bp = Blueprint('series_get', __name__, url_prefix='/api')

@bp.get('/series')
def series():
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

   cur.execute(
    """
    SELECT * FROM ka_series
    """
   )
   try:
      data = cur.fetchall()
      
      conn.commit()
      cur.close()
      conn.close()

      FIELDNAMES = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
      data_factory = [dict(zip(FIELDNAMES, row)) for row in data]

      return {'Data': data_factory}, HTTPStatus.OK
   except:
      return {'Data': data}, HTTPStatus.OK