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
    SELECT * FROM ka_series
    """
   )
   data = cur.fetchall()
   FIELDNAMES = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
   data_factory = [dict(zip(FIELDNAMES, row)) for row in data]

   conn.commit()
   cur.close()
   conn.close()

   return {'Data': data_factory}, HTTPStatus.CREATED